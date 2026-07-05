from flask import Flask, jsonify, request
from external_api import fetch_by_barcode, fetch_by_name

app = Flask(__name__)

#Simulate in memorry data using a list
inventory = [
    {
        "id": 1,
        "name": "Nutella",
        "brand": "Ferrero",
        "category": "Chocolate spreads",
        "barcode": "3017620422003",
        "quantity": 20,
        "price": 500.0,
        "image": "https://images.openfoodfacts.org/images/products/301/762/042/2003/front_en.879.400.jpg",
        "source": "OpenFoodFacts"
    },
    {
        "id": 2,
        "name": "Coca-Cola",
        "brand": "The Coca-Cola Company",
        "category": "Soft drinks",
        "barcode": "5449000000996",
        "quantity": 50,
        "price": 120.0,
        "image": "https://images.openfoodfacts.org/images/products/544/900/000/0996/front_en.500.400.jpg",
        "source": "OpenFoodFacts"
    },
    {
        "id": 3,
        "name": "Oreo",
        "brand": "Mondelez",
        "category": "Biscuits",
        "barcode": "7622210449283",
        "quantity": 35,
        "price": 180.0,
        "image": "https://images.openfoodfacts.org/images/products/762/221/044/9283/front_en.200.400.jpg",
        "source": "OpenFoodFacts"
    },
    {
        "id": 4,
        "name": "Milk",
        "brand": "Brookside",
        "category": "Dairy",
        "barcode": "6001009000012",
        "quantity": 15,
        "price": 75.0,
        "image": "",
        "source": "Manual"
    },
    {
        "id": 5,
        "name": "Bread",
        "brand": "Supa Loaf",
        "category": "Bakery",
        "barcode": "",
        "quantity": 25,
        "price": 65.0,
        "image": "",
        "source": "Manual"
    }
]

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

    # search for the product
    if data.get("barcode"):
        product = fetch_by_barcode(data["barcode"])
    elif data.get("name"):
        product = fetch_by_name(data["name"])
    else:
        return jsonify({"message": "Please provide a barcode or product name"}), 400
    
    #Generate new id
    new_id = max((item["id"] for item in inventory), default=0) + 1
    
    #Create item
    item = {
        "id": new_id,
        "name": data.get("name"),  
        "barcode": data.get("barcode"),
        "quantity": data["quantity"],
        "price": data["price"],
        "source": "Manual"
    }

    #Enhance the inventory with API data
    # If OpenFoodFacts found the product, enrich it
    if product:
        item.update(product)
        item["source"] = "OpenFoodFacts"
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
def delete_product(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Product deleted"}), 200

    return jsonify({"message": "Product not found"}), 404




#Finding a product using either barcode or name
@app.route("/search", methods=["GET"])
def search_product():
    barcode = request.args.get("barcode")
    name = request.args.get("name")

    if barcode:
        product = fetch_by_barcode(barcode)
    elif name:
        product = fetch_by_name(name)
    else:
        return jsonify({"message": "Please provide a barcode or product name"}), 400

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product), 200

if __name__ == "__main__":
    app.run(debug=True)