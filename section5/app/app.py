from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
from app_logging import AppLogger
from config_manager import ConfigManager
from connection.db import DbInit
import os

DEFAULT_PORT = 5050
logger = AppLogger(__name__).get_logger()

app = Flask(__name__)
app.secret_key = os.environ.get("JWT_SECRET", ConfigManager.get("jwt_secret", "jose"))

api = Api(app)
jwt = JWT(app, authenticate, identity)  # new endpont '/auth'
# Requires Authorization header
#   JWT <token>

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"message": f"An item with name {name} already exists."}, 400

        data = Item.parser.parse_args()

        # silent=True returns None if invalid Content-Type
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201  # 201 = created, 202 = accepted

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name), items)
        return {"message": "Item deleted"}

    # Create or Update Item
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)

        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200


# API Endpoints
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

# Server run
if __name__ == "__main__":
    ConfigManager.print_config()
    init_database = ConfigManager.get("init_database", False)
    if init_database:
        logger.info("init_database is True")
        DbInit.users()

    port = os.environ.get("WS_PORT", DEFAULT_PORT)
    app.run(port=port, host="0.0.0.0", debug=True)
