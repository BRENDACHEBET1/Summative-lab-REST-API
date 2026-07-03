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

