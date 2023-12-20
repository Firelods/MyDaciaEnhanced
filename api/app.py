import psycopg2
from flask import Flask

from account import init_renault_session
from scheduler import get_taches, planifier_tache_once, planifier_charge
from vehicle import set_vin, charge, get_car_info
from database import postgres_db

app = Flask(__name__)
app.route('/plan_charge', methods=['POST'])(planifier_charge)

app.route('/charge', methods=['POST'])(charge)

app.route('/get_taches', methods=['GET'])(get_taches)

app.route('/init_renault_session', methods=['POST'])(init_renault_session)

app.route('/plan_task_once', methods=['POST'])(planifier_tache_once)

app.route('/set_vin', methods=['POST'])(set_vin)

app.route('/get_car_info', methods=['GET'])(get_car_info)

if __name__ == "__main__":
    app.run(port=5000)
