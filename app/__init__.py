from flask import Flask
from .config import config
import os



def create_app():

    app = Flask(__name__)
    config_profile = os.environ.get("FLASK_ENV")

    app.config.from_object(config[config_profile])

    @app.route('/hello')
    def hello():
        return "Hello Docker"

    return app
