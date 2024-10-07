#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    #Query to GET all bakeries
    bakerie = [bakery.to_dict() for bakery in Bakery.query.all()]
    response = make_response(jsonify(bakerie), 200, {"Content-Type":"application/json"})
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    # Query for filter_by id
    bakerie = Bakery.query.filter(Bakery.id == id).first()
    bakerie_dict = bakerie.to_dict()
    response = make_response(jsonify(bakerie_dict), 200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    # Query for the price
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()  
    baked_good_dict = [good.to_dict() for good in baked_goods]
    response = make_response(jsonify(baked_good_dict), 200, {"Content-Type":"application/json"})
    return response

@app.route("/baked_goods/by_price/<float:price>")
def baked_goods_price_by_id(price):
    # Query for baked goods that match the specified price
    baked_goods = BakedGood.query.filter(BakedGood.price == price).all()
    baked_dicts = [good.to_dict() for good in baked_goods]
    response = make_response(jsonify(baked_dicts), 200)
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    # Query for the most expensive baked good
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    most_expensive_dict = most_expensive.to_dict()
    response = make_response(jsonify(most_expensive_dict), 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
