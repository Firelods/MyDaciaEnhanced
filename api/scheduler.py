from apscheduler.schedulers.background import BackgroundScheduler
from flask import request, g
from _datetime import datetime as dt
#from vehicle import charge

scheduler = BackgroundScheduler()
scheduler.start()

def planifier_charge():
    datetime = dt.fromisoformat(request.json['datetime'])  # datetime is a iso format string
    heure = datetime.hour
    minute = datetime.minute
    second = datetime.second

    token = g.token
    # scheduler.add_job(charge, 'cron',args=[token], hour=heure, minute=minute, second=second)
    return {"message": f"Tâche planifiée à {heure} heure(s)"}


def get_taches():
    jobs = scheduler.get_jobs()
    return {"jobs": str(jobs)}, 200

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



