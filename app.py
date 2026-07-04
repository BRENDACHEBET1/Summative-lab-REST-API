from flask import Flask, jsonify, request
from external_api import fetch_by_barcode, fetch_by_name

app = Flask(__name__)

#Simulate in memorry data using a list
inventory = []

#CRUD Operations
#GET all inventory
@app.route('/inventory', methods = ["GET"])
def get_inventory():
    return jsonify(inventory), 200

#Get a single item
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

    #Determine how to search for the product
    if data.get("barcode"):
        product = fetch_by_barcode(data["barcode"])
    elif data.get("name"):
        product = fetch_by_name(data["name"])
    else:
        return jsonify({"message": "Please provide a barcode or product name"}), 400

    # Check if the product was found
    if product is None:
        return jsonify({"message": "Product not found"}), 404
    
    #Generate new id
    new_id = max((item["id"] for item in inventory), default=0) + 1
    item = {
        "id": new_id,
        "name": data.get("name"),  
        "barcode": data.get("barcode"),
        "quantity": data["quantity"],
        "price": data["price"],
        "source": "OpenFoodFacts"
    }

    #Enhance the inventory with API data
    item.update(product)
    #Save the enhanced item
    inventory.append(item)
    

    return jsonify(item), 201

#Update item
@app.route('/inventory/<int:item_id>', methods=["PATCH"])
def update_product(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    allowed_fields = ["name", "barcode", "quantity", "price", "category"]


    for item in inventory:
        if item["id"] == item_id:

            for key, value in data.items():
                if key in allowed_fields:
                    item[key] = value

            return jsonify(item), 200

    return jsonify({"error": "Product not found"}), 404


#DElete item
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global inventory
    
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Product deleted"}), 200

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)