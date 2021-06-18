from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# STORES
stores  = [
    {
        'name': 'My Wonderful Store',
        'items':[
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# Render home
@app.route('/')
def home():
    return render_template("index.html")

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name']
        ,'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') # http://localhost:8080/store/store_name
def get_store(name):
    # Iterate over stores
    # If the store matches, return it
    # If None return error message
    store = [store for store in stores if store['name'] == name]
    if store is not None:
        return jsonify({'store': store})
    else:
        return jsonify({'message': 'Store not found, please try again!'})

# GET /store
@app.route('/store') # http://localhost:8080/store/
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name']
                ,'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify({'store': store})

    return jsonify({'message': 'Store not found, please try again!'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item') # http://localhost:8080/store/store_name/item
def get_items_in_store(name):

    for store in stores:
        if store['name'] == name:
            print(type(store))
            return jsonify( {'items':store['items'] } )
    return jsonify ({'message':'store not found'})

app.run(port=5050)