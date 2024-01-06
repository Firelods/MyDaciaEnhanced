from account import init_renault_session, login
from api.middleware import token_required
from api.scheduler import planifier_charge, get_planified_tasks_for_user
from vehicle import set_vin, charge, get_car_info, sync_charge, get_past_tasks_for_user


def set_up_routes(app, scheduler):
    @app.route('/plan_charge', methods=['POST'])
    def plan_charge():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return planifier_charge(login_id, scheduler,sync_charge)

    @app.route('/charge', methods=['POST'])
    def charge_route():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return charge(login_id)

    @app.route('/get_taches', methods=['GET'])
    def get_taches_route():
        if not scheduler.running:
            return {"error": "Scheduler is not running"}, 500
        jobs = scheduler.get_jobs()
        scheduler.print_jobs()
        return {"jobs": str(jobs)}, 200

    @app.route('/get_taches', methods=['GET'])
    def get_taches_for_user_route():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return get_planified_tasks_for_user(login_id, scheduler)

    @app.route('/login', methods=['POST'])
    def login_route():
        return login()

    @app.route('/init_renault_session', methods=['POST'])
    async def init_renault_session_route():
        return await init_renault_session()

    @app.route('/set_vin', methods=['POST'])
    def set_vin_route():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return set_vin(login_id)

    @app.route('/car_info', methods=['GET'])
    async def get_car_info_route():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return await get_car_info(login_id,scheduler)

    @app.route('/get_past_tasks', methods=['GET'])
    def get_past_tasks_route():
        try:
            login_id = token_required()
        except Exception as e:
            return {"message": str(e)}, 400
        return get_past_tasks_for_user(login_id)
