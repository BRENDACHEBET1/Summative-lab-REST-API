from flask import Flask, jsonify, request

app = Flask(__name__)

#Simulate in memorry data using a list
inventory = []

#CRUD Operations
#GET all inventory
@app.route('/inventory', methods = ["GET"])
def get_inventory():
    return jsonify(inventory), 200

#Get a single product
@app.route('/inventory/<int:item_id>', methods= ["GET"])
def get_product(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200
        
    return jsonify({"error": "Product not found"}), 404

#Add a product
@app.route('/inventory', methods=["POST"])
def add_product():
    data = request.get_json()
    new_id = max((item.id for item in inventory), default=0) + 1

    item = {
        "id": new_id,
        "name": data["name"],
        "barcode": data.get("barcode"),
        "quantity": data["quantity"],
        "price": data["price"],
        "category": data["category"],
        "source": "manual"
    }

    inventory.append(item)
    

    return jsonify(item), 201

#Update product
@app.route('inventory/<int:item_id>', methods=["PATCH"])
def update_product(item_id):
    data = request.get_json()

    for item in inventory:
        if item["id"] == item_id:
            item.upadte(data)
            return jsonify(item)
        
    return("Not found", 404)

#DElete product
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]
    return jsonify({"message": "deleted"})