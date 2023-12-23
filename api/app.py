from flask import Flask
from flask_cors import CORS

from account import init_renault_session, login
from api.middleware import token_required
from scheduler import get_taches, planifier_tache_once, planifier_charge
from vehicle import set_vin, charge, get_car_info

app = Flask(__name__)
CORS(app)


@app.route('/plan_charge', methods=['POST'])
def plan_charge():
    return planifier_charge()


@app.route('/charge', methods=['POST'])
def charge_route():
    return charge()


@app.route('/get_taches', methods=['GET'])
def get_taches_route():
    return get_taches()


@app.route('/login', methods=['POST'])
def login_route():
    return login()


@app.route('/init_renault_session', methods=['POST'])
async def init_renault_session_route():
    return await init_renault_session()


@app.route('/plan_task_once', methods=['POST'])
def plan_task_once_route():
    return planifier_tache_once()


@app.route('/set_vin', methods=['POST'])
def set_vin_route():
    try:
        login_id = token_required()
    except Exception as e:
        print(str(e))

        return {"message": str(e)}, 400
    return set_vin(login_id)


@app.route('/car_info', methods=['GET'])
async def get_car_info_route():
    try:
        login_id = token_required()
    except Exception as e:
        return {"message": str(e)}, 400
    return await get_car_info(login_id)


if __name__ == "__main__":
    app.run(port=5000)
