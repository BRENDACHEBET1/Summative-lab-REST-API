from flask import Flask, jsonify, request

app = Flask(__name__)

#Simulate in memorry data using a list
products = []

#CRUD Operations
#GET all products
@app.route('/products', methods = ["GET"])
def get_products():
    return jsonify(products), 200

#Get a single product
@app.route('/products/<int: id>', methods= ["GET"])
def get_product(id):
    for p in products:
        if p["id"] == id:
            return jsonify(p), 200
        
    return jsonify({"error": "Product not found"}), 404

#Add a product
@app.route('/products', methods=["POST"])
def add_product():
    data = request.get_json()
    new_id = max((p.id for p in products), default=0) + 1

    item = {
        "id": new_id,
        "name": data["name"],
        "barcode": data.get("barcode"),
        "quantity": data["quantity"],
        "price": data["price"],
        "category": data["category"],
        "source": "manual"
    }

    products.append(item)
    

    return jsonify(item), 201