import string
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name",
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {
                "message": f"A store with name {name} already exists."
            }, 400

        # silent=True returns None if invalid Content-Type
        store = StoreModel(name=name)
        try:
            store.upsert()
        except Exception:
            return {
                "message": "An error occurred while creating the store"
            }, 500
        return store.json(), 201  # 201 = created, 202 = accepted

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()

        return {"message": "Store deleted"}, 200

    # Create or Update Item
    @jwt_required()
    def put(self, name):
        data = Store.parser.parse_args()
        store = StoreModel.find_by_name(name)

        if store is None:
            try:
                store = StoreModel(name, **data)
            except Exception:
                return {"message": "An error occurred"}, 500

        store.upsert()
        return store.json(), 204


class StoreList(Resource):
    def get(self):
        return {
            "stores": [store.json() for store in StoreModel.query.all()]
        }, 200
