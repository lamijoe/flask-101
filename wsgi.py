# wsgi.py
# pylint: disable=missing-docstring

#from crypt import methods
from pickle import GET
from flask import Flask, jsonify, abort, request
import itertools

app = Flask(__name__)

BASE_URL = "/api/v1"

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Nature Channel'}
}

@app.route('/')
def hello():
    return "Hello Joe!"

@app.route(f'{BASE_URL}')
def bienvenue():
    return "Bienvenue sur l'API"

@app.route(f'{BASE_URL}/products')
def products():
    #return "liste des produits"
    return PRODUCTS

@app.route(f"{BASE_URL}/products", methods = ['GET'])
def read_many_product():
    products = list(PRODUCTS.values())
    return jsonify(products), 200

@app.route(f"{BASE_URL}/products/<int:product_id>", methods = ['GET'])
def read_one_product(product_id):
    product = PRODUCTS.get(product_id)
    print(f"product_id = {product}")
    if product is None:
        abort(404)
    
    return jsonify(product), 200
        
