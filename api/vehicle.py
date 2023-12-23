import asyncio
import datetime
import aiohttp
from flask import request, g
from renault_api.kamereon.enums import ChargeState
from renault_api.renault_client import RenaultClient
from account import get_login_id_from_token, get_password_from_database, get_account_id_from_database
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


async def charge():
    token = g.token
    login_id = get_login_id_from_token(token)
    password = get_password_from_database(login_id)
    vin = get_vin_from_database(token)
    account_id = get_account_id_from_database(login_id)
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account = await client.get_api_account(account_id)
        vehicle = await account.get_api_vehicle(vin)
        try:
            charge_start = await vehicle.set_charge_start()
            print(charge_start)
        except:
            return {"message": "Erreur lors du lancement de la charge"}, 400
        # wait 10 seconds for the charge to start
        await asyncio.sleep(5)
        # check if charge is started
        charge_status = await vehicle.get_battery_status()
        print(charge_status.get_charging_status())
        if charge_status.get_charging_status() == ChargeState.CHARGE_IN_PROGRESS:
            success = True
            error_message = ""
        else:
            success = False
            error_message = "La charge n'a pas démarré"
        cursor = postgres_db.cursor()
        postgres_insert_query = """ INSERT INTO logs_actions(action,created_at,success,login_id,informations) 
                                    VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = ("charge", datetime.datetime.now(), success, login_id, error_message)
        cursor.execute(postgres_insert_query, record_to_insert)
        postgres_db.commit()
        cursor.close()
        if success:
            return {"message": "Charge lancée", "informations": error_message}, 200
        else:
            return {"message": "Erreur lors du lancement de la charge", "informations": error_message}, 400


async def get_car_info(login_id):
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
            # export interface CarInfo {
            #   name: string;
            #   autonomy: number;
            #   imageUrl: string;
            #   charging: boolean;
            #   climate: boolean;
            #   lastRefresh: Date;
            #   totalKilometers: number;
            #   batteryLevel: number;
            #   scheduled: { airConditioning: ScheduledTask, charging: ScheduledTask };
            # }
            # return a json like this
            return {"name": details.model.label, "autonomy": battery_status.batteryAutonomy,
                    "imageUrl": "https://static.renault.co.uk/cms/version/2021-01/renault-logo-2020.png",
                    "charging": battery_status.get_charging_status() == ChargeState.CHARGE_IN_PROGRESS,
                    "climate": hvac_status.hvacStatus == "ON",
                    "lastRefresh": battery_status.timestamp,
                    "totalKilometers": cockpit.totalMileage,
                    "batteryLevel": battery_status.batteryLevel,
                    }, 200
        except Exception as e:
            print(str(e))
            return {"message": "Erreur lors de la récupération des informations", "erreur": str(e)}, 400
