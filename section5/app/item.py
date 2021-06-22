from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from connection.db import DbConnection

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item, 200
        return {'message': 'item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        with DbConnection() as db:
            query = "SELECT * FROM items WHERE name = ?"
            result = db.cursor.execute(query, (name,))
            row = result.fetchone()
            
            if row:
                return {'item': {'id': row[0], 'name': row[1], 'price': row[2]}}

    @classmethod
    def find_by_id(cls, _id):
        with DbConnection() as db:
            query = "SELECT * FROM items WHERE id = ?"
            result = db.cursor.execute(query, (_id,))
            row = result.fetchone()
            
            if row:
                return {'item': {'id': row[0], 'name': row[1], 'price': row[2]}}

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"An item with name {name} already exists."}, 400

        data = Item.parser.parse_args()

        # silent=True returns None if invalid Content-Type
        item = {"name": name, "price": data["price"]}
        with DbConnection() as db:
            query = "INSERT INTO items VALUES (NULL, ?, ?)"
            db.cursor.execute(query, (item["name"], item["price"]))
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
