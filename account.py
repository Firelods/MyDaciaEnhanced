import datetime
import aiohttp
import jwt
import psycopg2
from cryptography.fernet import Fernet
from flask import request
from renault_api.renault_client import RenaultClient
from database import postgres_db


def load_key():
    """
    Loads the key named `key.key` from the current directory.
    """
    return open("key.key", "rb").read()


def save_key(key):
    """
    Saves the key to a file named `key.key` in the current directory.
    """
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Check if key exists
try:
    key = load_key()
except FileNotFoundError:
    # If not, generate a new key
    key = Fernet.generate_key()
    save_key(key)

cipher_suite = Fernet(key)
SECRET_KEY = "your-secret-key"  # replace with your secret key


async def init_renault_session():
    if request.json['login_id'] is None:
        return {"message": "Le login_id n'est pas spécifié"}, 400
    if request.json['password'] is None:
        return {"message": "Le mot de passe n'est pas spécifié"}, 400
    login_id = request.json['login_id']
    password = request.json['password']
    async with aiohttp.ClientSession() as websession:
        client = RenaultClient(websession=websession, locale="fr_FR")
        await client.session.login(login_id, password)
        account_list = (await client.get_person()).accounts
        account_id = ""
        # add every accountID in list
        for account in account_list:
            if account.accountType == "MYDACIA":
                account_id = account.accountId
                account = await client.get_api_account(account_id)
                vehicle_list = (await account.get_vehicles()).vehicleLinks
                # add every vin in list
                vehicle_list_to_return = []
                for vehicle in vehicle_list:
                    vin = vehicle.vin
                    vehicle = await account.get_api_vehicle(vin)
                    vehicle_details = await vehicle.get_details()
                    vehicle_list_to_return.append({"model": vehicle_details.model.label, "vin": vin,
                                                   "licensePlate": vehicle_details.registrationNumber})
                # Generate JWT token
                payload = {
                    "login_id": login_id,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                # Hash password and store it
                encrypted_password = cipher_suite.encrypt(password.encode())
                print("encrypted_password: ", encrypted_password)
                # save in postgresql database
                cursor = postgres_db.cursor()
                postgres_insert_query = """ INSERT INTO mobile_user (login_id, password,account_id) VALUES (%s,%s,%s)"""
                record_to_insert = (login_id, psycopg2.Binary(encrypted_password), account_id)
                cursor.execute(postgres_insert_query, record_to_insert)
                postgres_db.commit()
                cursor.close()
                return {"vehicles": vehicle_list_to_return, "token": token}
        return {"message": "Aucun compte n'a été trouvé"}, 404


def get_account_id_from_database(login_id):
    cursor = postgres_db.cursor()
    postgres_select_query = """ SELECT account_id FROM mobile_user WHERE login_id = %s"""
    cursor.execute(postgres_select_query, (login_id,))
    account_id = cursor.fetchone()[0]
    cursor.close()
    return account_id


def get_password_from_database(login_id):
    cursor = postgres_db.cursor()
    postgres_select_query = """ SELECT password FROM mobile_user WHERE login_id = %s"""
    cursor.execute(postgres_select_query, (login_id,))
    encrypted_password = bytes(cursor.fetchone()[0])
    print("encrypted_password: ", encrypted_password)
    cursor.close()
    password = cipher_suite.decrypt(encrypted_password).decode()

    return password


def get_login_id_from_token(token):
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
    login_id = decoded_token["login_id"]
    return login_id
