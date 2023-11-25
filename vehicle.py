import datetime

import aiohttp
from flask import request
from renault_api.renault_client import RenaultClient
from account import get_login_id_from_token, get_password_from_database
from database import postgres_db


def set_vin(token):
    login_id = get_login_id_from_token(token)
    vin = request.json['vin']
    cursor = postgres_db.cursor()
    postgres_update_query = """ UPDATE mobile_user SET vin = %s WHERE login_id = %s"""
    cursor.execute(postgres_update_query, (vin, login_id))
    postgres_db.commit()
    cursor.close()
    return {"message": "VIN enregistré"}, 204


def get_vin_from_database(token):
    login_id = get_login_id_from_token(token)
    cursor = postgres_db.cursor()
    postgres_select_query = """ SELECT vin FROM mobile_user WHERE login_id = %s"""
    cursor.execute(postgres_select_query, (login_id,))
    vin = cursor.fetchone()[0]
    cursor.close()
    return vin


async def charge(token):
    login_id = get_login_id_from_token(token)
    password = get_password_from_database(login_id)
    vin = get_vin_from_database(token)
    account_id = request.json['account_id']
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account = await client.get_api_account(account_id)
        vehicle = await account.get_api_vehicle(vin)
        try:
            await vehicle.set_charge_start()
            # add the action in database
            success = True
        except:
            success = False

        cursor = postgres_db.cursor()
        postgres_insert_query = """ INSERT INTO logs_actions(action,created_at,success,login_id) VALUES (%s,%s,%s,%s)"""
        record_to_insert = ("charge", datetime.datetime.now(), success, login_id)
        cursor.execute(postgres_insert_query, record_to_insert)
        postgres_db.commit()
        cursor.close()
