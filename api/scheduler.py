import logging
from datetime import datetime, timezone

from apscheduler.triggers.date import DateTrigger
from flask import request


def planifier_charge(login_id, scheduler, sync_charge):
    datetime2 = datetime.fromisoformat(request.json['datetime'])  # datetime is an iso format string
    if datetime2 < datetime.now(timezone.utc):
        logging.error("Date cannot be in the past")
        return {"message": "La date ne peut pas être dans le passé"}, 400

    scheduler.add_job(sync_charge, DateTrigger(run_date=datetime2), args=[login_id])
    scheduler.print_jobs()
    return {
        "message": f"Tâche planifiée à {datetime2.hour} heure(s) {datetime2.minute} minute(s) {datetime2.second} seconde(s)"}, 201


def get_planified_tasks_for_user(login_id, scheduler):
    # return all tasks for a use in a json format
    jobs = scheduler.get_jobs()
    # filter jobs by login_id
    jobs = [job for job in jobs if job.kwargs['login_id'] == login_id]
    return jobs
