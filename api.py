from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler

import aiohttp
import asyncio

from renault_api.kamereon.models import ChargeSchedule, ChargeDaySchedule
from renault_api.renault_client import RenaultClient

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()


def ma_tache():
    print("Tâche exécutée !")


@app.route('/planifier_tache', methods=['POST'])
def planifier_tache():
    datetime = request.json['datetime']  # get datetime from request in JS format
    heure = datetime.hour
    minute = datetime.minute
    second = datetime.second
    scheduler.add_job(ma_tache, 'cron', hour=heure, minute=minute, second=second)
    return {"message": f"Tâche planifiée à {heure} heure(s)"}


@app.route('/get_taches', methods=['GET'])
def get_taches():
    jobs = scheduler.get_jobs()
    return {"jobs": str(jobs)}


@app.route('/init_renault_session', methods=['POST'])
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
                return {"vehicles": vehicle_list_to_return}
        return {"message": "Aucun compte n'a été trouvé"}, 404


# function to plan a task at a specific time just once

@app.route('/plan_task_once', methods=['POST'])
def planifier_tache_once():
    if request.json['datetime'] is None:  # check if datetime is specified
        return {"message": "La date n'est pas spécifiée"}, 400
    datetime = request.json['datetime']
    if datetime < datetime.now():
        return {"message": "La date est déjà passée"}, 400
    else:
        if request.json["type"] is None:
            return {"message": "Le type de tâche n'est pas spécifié"}, 400
        if request.json["type"] == "charge":
            if request.json["login_id"] is None:
                return {"message": "Le login_id n'est pas spécifié"}, 400
            if request.json["password"] is None:
                return {"message": "Le mot de passe n'est pas spécifié"}, 400
            if request.json["vin"] is None:
                return {"message": "Le vin n'est pas spécifié"}, 400
            # scheduler.add_job(launch_charge(login_id=request.json["login_id"], password=["password"]), 'date',
            #                   run_date=datetime)
            return {"message": "Tâche planifiée"}


if __name__ == "__main__":
    app.run(port=5000)
