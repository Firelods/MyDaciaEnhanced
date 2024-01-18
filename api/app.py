from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_cors import CORS
import logging

from routes import set_up_routes

scheduler = BackgroundScheduler()
scheduler.start()

app = Flask(__name__)
CORS(app)
set_up_routes(app, scheduler)
# Configure logging
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


if __name__ == "__main__":
    app.run(port=5000)
