from flask import Flask, jsonify
from flask.config import Config
from flask_restful import Api
from flask_jwt import JWT
import os, sys
from security import authenticate, identity as identity_function
from resources.user import UserRegister
from app_logger import AppLogger
from connection.db import DbInit
from resources.item import Item, ItemList
from datetime import timedelta
from config_manager import ConfigManager
import logging

DEFAULT_PORT = 5050
logger = AppLogger.get_logger(__name__)

ConfigManager.init()
app = Flask(__name__)
app.secret_key = os.environ.get("JWT_SECRET", ConfigManager.get("jwt_secret", "jose"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
# app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=3600)  # 1 hour expiration time
# app.logger.addHandler()

for logr in (app.logger, logging.getLogger("werkzeug")):
    logr.addHandler(AppLogger.file_handler())
    logr.addHandler(AppLogger.console_handler())

# config JWT auth key name to be 'email' instead of default 'username'
app.config["JWT_AUTH_USERNAME_KEY"] = "email"

jwt = JWT(app, authenticate, identity_function)  # new endpont '/auth'
# Requires Authorization header
#   JWT <token>


@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify(
        {"access_token": access_token.decode("utf-8"), "user_id": identity.id}
    )


# API Endpoints
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

# Server run
if __name__ == "__main__":
    from connection.db import db

    db.init_app(app)
    ConfigManager.print_config()

    init_database = os.environ.get("INIT_DB")
    if init_database == "1":
        logger.info("init_database triggered")
        DbInit.all()

    port = os.environ.get("WS_PORT", DEFAULT_PORT)
    app.run(port=port, host="0.0.0.0")
