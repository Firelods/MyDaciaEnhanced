import logging
from datetime import datetime

import asyncio
import aiohttp
from flask import request
from renault_api.kamereon.enums import ChargeState
from renault_api.renault_client import RenaultClient

from account import get_password_from_database, get_account_id_from_database
from api.scheduler import get_planified_tasks_for_user
from database import postgres_db


def set_vin(login_id):
    vin = request.json['vin']
    cursor = postgres_db.cursor()
    postgres_update_query = """ UPDATE mobile_user SET vin = %s WHERE login_id = %s"""
    cursor.execute(postgres_update_query, (vin, login_id))
    postgres_db.commit()
    cursor.close()
    return {"message": "VIN enregistré"}, 204


def get_vin_from_database(login_id):
    cursor = postgres_db.cursor()
    postgres_select_query = """ SELECT vin FROM mobile_user WHERE login_id = %s"""
    cursor.execute(postgres_select_query, (login_id,))
    vin = cursor.fetchone()[0]
    cursor.close()
    return vin


async def charge(login_id):
    password = get_password_from_database(login_id)
    vin = get_vin_from_database(login_id)
    account_id = get_account_id_from_database(login_id)
    logging.info("Starting charge for user %s", login_id)
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account = await client.get_api_account(account_id)
        vehicle = await account.get_api_vehicle(vin)
        logging.info("Vehicle to charge retrieved: %s", vehicle)
        try:
            charge_start = await vehicle.set_charge_start()
            logging.info("Charge started: %s", charge_start)
        except:
            logging.error("Error while starting charge")
            return {"message": "Erreur lors du lancement de la charge"}, 400
        # wait 10 seconds for the charge to start
        success = True
        error_message = ""
        cursor = postgres_db.cursor()
        postgres_insert_query = """ INSERT INTO logs_actions(action,created_at,success,login_id,informations) 
                                    VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = ("charge", datetime.now(), success, login_id, error_message)
        try:
            cursor.execute(postgres_insert_query, record_to_insert)
            logging.info("Action saved in database")
        except:
            cursor.close()
            logging.error("Error while saving action in database")
            return {"message": "Erreur lors de l'enregistrement de l'action"}, 400
        postgres_db.commit()
        cursor.close()
        if success:
            return {"message": "Charge lancée", "informations": error_message}, 200
        else:
            return {"message": "Erreur lors du lancement de la charge", "informations": error_message}, 400


async def get_car_info(login_id, scheduler):
    password = get_password_from_database(login_id)
    vin = get_vin_from_database(login_id)
    if vin is None:
        return {"message": "Aucun véhicule n'est enregistré"}, 400
    account_id = get_account_id_from_database(login_id)
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account = await client.get_api_account(account_id)
        vehicle = await account.get_api_vehicle(vin)
        try:
            cockpit = await vehicle.get_cockpit()
            battery_status = await vehicle.get_battery_status()
            hvac_status = await vehicle.get_hvac_status()
            details = await vehicle.get_details()
            scheduled = get_planified_tasks_for_user(login_id, scheduler)

            return {"name": details.model.label, "autonomy": battery_status.batteryAutonomy,
                    "imageUrl": "https://static.renault.co.uk/cms/version/2021-01/renault-logo-2020.png",
                    "charging": battery_status.get_charging_status() == ChargeState.CHARGE_IN_PROGRESS,
                    "climate": hvac_status.hvacStatus == "ON",
                    "lastRefresh": battery_status.timestamp,
                    "totalKilometers": cockpit.totalMileage,
                    "batteryLevel": battery_status.batteryLevel,
                    "scheduled": scheduled,
                    "history": get_past_tasks_for_user(login_id)
                    }, 200
        except Exception as e:
            print(str(e))
            return {"message": "Erreur lors de la récupération des informations", "erreur": str(e)}, 400


def sync_charge(login_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(charge(login_id))
    loop.close()
    return result


def get_past_tasks_for_user(login_id):
    # search in logs_actions table for past tasks
    postgres_select_query = """ SELECT * FROM logs_actions WHERE login_id = %s"""
    cursor = postgres_db.cursor()
    try:
        cursor.execute(postgres_select_query, (login_id,))
    except:
        cursor.close()
        logging.error("Error while retrieving past tasks for user %s", login_id)
        return {"message": "Erreur lors de la récupération des tâches passées"}, 500
    records = cursor.fetchall()
    cursor.close()
    # make a json from the records
    records_json = []
    for record in records:
        record_json = {
            "action": record[1],
            "created_at": record[2],
            "success": record[3],
            "login_id": record[4],
            "informations": record[5]
        }
        records_json.append(record_json)
    return records_json
