from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from connection.db import DbConnection
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!",
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message": "item not found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                "message": f"An item with name {name} already exists."
            }, 400

        data = Item.parser.parse_args()

        # silent=True returns None if invalid Content-Type
        item = ItemModel(name=name, price=data["price"])
        try:
            item.insert()
        except Exception:
            return {"message": "An error occurred"}, 500
        return item.json(), 201  # 201 = created, 202 = accepted

    @jwt_required()
    def delete(self, name):
        with DbConnection() as db:
            query = "DELETE FROM items WHERE name = ?"
            db.cursor.execute(query, (name,))

        return {"message": "Item deleted"}, 200

    # Create or Update Item
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name=name, price=data["price"])

        if item is None:
            try:
                updated_item.insert()
            except Exception:
                return {"message": "An error occurred"}, 500
        else:
            try:
                updated_item.update()
            except Exception:
                return {"message": "An error occurred"}, 500
        return updated_item.json(), 204


class ItemList(Resource):
    def get(self):
        with DbConnection() as db:
            query = "SELECT * FROM items"
            result = db.cursor.execute(query)
            results = result.fetchall()

            items = []
            for i in results:
                items.append({"id": i[0], "name": i[1], "price": i[2]})

        return {"items": items}, 200
