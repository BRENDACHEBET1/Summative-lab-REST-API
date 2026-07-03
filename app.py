from flask import Flask, jsonify, request

app = Flask(__name__)

#Simulate in memorry data using a list
products = []

#CRUD Operations
#GET all products
@app.route('/products', methods = ["GET"])
def get_products():
    return jsonify(products), 200