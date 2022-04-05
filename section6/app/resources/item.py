from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument(
        "store_id",
        type=int,
        required=True,
        help="Every item needs a store_id",
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
        item = ItemModel(name=name, **data)
        try:
            item.upsert()
        except Exception:
            return {"message": "An error occurred"}, 500
        return item.json(), 201  # 201 = created, 202 = accepted

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()

        return {"message": "Item deleted"}, 200

    # Create or Update Item
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            try:
                item = ItemModel(name, **data)
            except Exception:
                return {"message": "An error occurred"}, 500
        else:
            try:
                item.price = data["price"]
            except Exception:
                return {"message": "An error occurred"}, 500

        item.upsert()
        return item.json(), 204


class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}, 200

        # with lambda
        # return {
        #     "items": list(map(lambda x: x.json(), ItemModel.query.all()))
        # }, 200
