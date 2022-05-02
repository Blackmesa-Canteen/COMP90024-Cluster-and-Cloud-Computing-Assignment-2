# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo_restful_controller
   Description :  TODO
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""
from service.database import Database
from flask import Flask, Blueprint, abort, jsonify, request

aurin_controller = Blueprint('aurin_controller', __name__)
server = Database()
books = []


@aurin_controller.route('/rai', methods=['GET'])
def get_rai():
    server.connect()
    result = server.get_rai()
    data = result['rows']
    processed_data = []
    for each in data:
        processed_data.append({each['key']: each['value']})
    return jsonify(processed_data)


@aurin_controller.route('/income', methods=['GET'])
def get_income():
    server.connect()
    return server.get_income()

@aurin_controller.route('/income/<view>', methods=['GET'])
def get_income_with_view(view):
    server.connect()
    result = server.get_income(view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    print(data)
    return jsonify(data)

@aurin_controller.route('/house-price', methods=['GET'])
def get_house_price():
    server.connect()
    return server.get_house_price()

@aurin_controller.route('/house-price/<type>/<view>', methods=['GET'])
def get_house_price_with_view(type, view):
    server.connect()
    result = server.get_house_price(type, view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    print(data)
    return jsonify(data)

