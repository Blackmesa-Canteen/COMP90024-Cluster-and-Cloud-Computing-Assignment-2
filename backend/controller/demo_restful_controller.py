# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo_restful_controller
   Description :  TODO
   Author :       Xiaotian Li
   date：          14/04/2022
-------------------------------------------------
"""

from flask import Flask, Blueprint, abort, jsonify, request

demo_restful_controller = Blueprint('demo_restful_controller', __name__)

# demo data
books = [
    {
        'id': 1,
        'title': u'论语',
        'author': u'孔子',
        'price': 18
    },
    {
        'id': 2,
        'title': u'道德经',
        'author': u'老子',
        'price': 15
    }
]


@demo_restful_controller.route('/book/', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@demo_restful_controller.route('/book/<int:id>', methods=['GET'])
def get_book_by_id(id):  # put application's code here
    for book in books:
        if book['id'] == id:
            return jsonify({'book': book})
    abort(404)


@demo_restful_controller.route('/book/', methods=['POST'])
def create_book():
    if not request.form or not 'title' in request.form:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.form['title'],
        'author': request.form['author'],
        'price': request.form['price'],
    }
    books.append(book)
    return jsonify({'book': book}), 201


@demo_restful_controller.route('/book/<int:id>', methods=['PUT'])
def update_book_by_id(id):
    for book in books:
        if book['id'] == id:
            book["title"] = request.form['title']
            book["author"] = request.form['author']
            book["price"] = request.form['price']
        return jsonify({'books': books})
    abort(400)


@demo_restful_controller.route('/book/<int:id>', methods=['DELETE'])
def delete_book_by_id(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})
