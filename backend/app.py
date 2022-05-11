# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     app
   Description :  main application entrance
   Author :       Xiaotian Li, Bocan Yang
   Date:          14/04/2022
-------------------------------------------------
"""
from flask import Flask
from flask_cors import CORS

from controller.demo_controller import demo_controller
from controller.aurin_controller import aurin_controller
from controller.twitter_controller import twitter_controller
from controller.scenario_controller import scenario_controller


app = Flask(__name__)
CORS(app)


# route register
app.register_blueprint(demo_controller, url_prefix='')
app.register_blueprint(aurin_controller, url_prefix='/api/aurin')
app.register_blueprint(twitter_controller, url_prefix='/api/twitter')
app.register_blueprint(scenario_controller, url_prefix='/api/scenario')


# handle 404 error
@app.errorhandler(404)
def handle404(err):
   return 'your request is wrong, please try again'


# handle 500 error
@app.errorhandler(500)
def handle500(err):
   return 'server data error, please contact the administrator'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
