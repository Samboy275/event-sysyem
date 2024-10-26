from flask import Flask
from flask_pymongo import MongoClient
from flask_jwt_extended import JWTManager
from .config import config
from .views.auth_views import auth_bp
from .views.organization_views import org_bp
import os
from datetime import timedelta


def create_app():

    app = Flask(__name__)
    config_profile = os.environ.get("FLASK_ENV", "development")

    app.config.from_object(config[config_profile])
    jwt = JWTManager(app)

    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=60)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
    app.register_blueprint(auth_bp)
    app.register_blueprint(org_bp)
    @app.route('/hello')
    def hello():
        return "Hello Docker"

    return app
