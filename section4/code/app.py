from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # new endpont '/auth'

items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price'
        ,type=float
        ,required=True
        ,help="This field cannot be left blank!")
    
    item_data = parser.parse_args()

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': 'An item with name {} already exists.'.format(name)}, 400

        # silent=True returns None if invalid Content-Type
        item_data = Item.parser.parse_args()
        item = {
            'name': name
            ,'price':item_data['price']
            }
        items.append(item)
        return item, 201  # 201 = created, 202 = accepted

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name), items)
        return {'message': 'Item deleted'}

    # Create or Update Item
    # @jwt_required()
    def put(self, name):
        Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)

        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(item_data)
        return item



class ItemList(Resource):
    def get(self):
        return {'items': items}, 200

# API Endpoints
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# Server run
if __name__ == '__main__':
    app.run(port=5000, debug=True)