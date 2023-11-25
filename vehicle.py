import aiohttp
from flask import request
from renault_api.renault_client import RenaultClient
from account import get_login_id_from_token, get_password_from_database
from database import postgres_db


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
    vin = request.json['vin']
    account_id = request.json['account_id']
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account = await client.get_api_account(account_id)
        vehicle = await account.get_api_vehicle(vin)
        await vehicle.set_charge_start()
