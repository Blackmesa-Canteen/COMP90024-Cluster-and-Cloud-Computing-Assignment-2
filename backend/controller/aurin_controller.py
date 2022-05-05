# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     aurin_controller
   Description :  Controller for aurin API handling
   Author :       Xiaotian Li, Bocan Yang
   Date:          14/04/2022
-------------------------------------------------
"""
from service.database import Database
from flask import Blueprint, abort, jsonify

aurin_controller = Blueprint('aurin_controller', __name__)
server = Database()


# Get all house price (RAI) data
@aurin_controller.route('/rai', methods=['GET'])
def get_rai():
    server.connect()
    result = server.get_rai()
    data = result['rows']
    processed_data = []
    for each in data:
        processed_data.append({each['key']: each['value']})
    return jsonify(processed_data)


# Get all incom data
@aurin_controller.route('/income', methods=['GET'])
def get_income():
    server.connect()
    return server.get_income()


# Get specific view of income data
@aurin_controller.route('/income/<view>', methods=['GET'])
def get_income_with_view(view):
    server.connect()
    result = server.get_income(view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    return jsonify(data)


# Get all house price data
@aurin_controller.route('/house-price', methods=['GET'])
def get_house_price():
    server.connect()
    return server.get_house_price()


# Get specific view of house price data
@aurin_controller.route('/house-price/<type>/<view>', methods=['GET'])
def get_house_price_with_view(type, view):
    server.connect()
    result = server.get_house_price(type, view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    return jsonify(data)

# Get all house migration(foreigner) data
@aurin_controller.route('/migration', methods=['GET'])
def get_migration():
    server.connect()
    return server.get_migration()


@aurin_controller.route('/migration/<view>', methods=['GET'])
def get_migration_with_view(view):
    server.connect()
    result = server.get_migration(view)
    try:
        data = result['rows']
    except KeyError:
        abort(404)
    return jsonify(data)