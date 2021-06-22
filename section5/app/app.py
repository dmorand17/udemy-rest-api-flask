from flask import Flask
from flask.config import Config
from flask_restful import  Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from app_logging import AppLogger
from config_manager import ConfigManager
from connection.db import DbInit
from item import Item, ItemList
import os

DEFAULT_PORT = 5050
logger = AppLogger.get_logger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("JWT_SECRET", ConfigManager.get("jwt_secret", "jose"))

api = Api(app)
jwt = JWT(app, authenticate, identity)  # new endpont '/auth'
# Requires Authorization header
#   JWT <token>

# API Endpoints
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

# Server run
if __name__ == "__main__":
    logger.info(f"configmanager {ConfigManager.getInstance()}")
    ConfigManager.print_config()
    init_database = ConfigManager.get("init_database", False)
    if init_database:
        logger.info("init_database triggered")
        DbInit.users()

    port = os.environ.get("WS_PORT", DEFAULT_PORT)
    app.run(port=port, host="0.0.0.0", debug=True)
