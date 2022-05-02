from flask import Flask

from controller.demo_controller import demo_controller
from controller.aurin_controller import aurin_controller
from controller.twitter_controller import twitter_controller

app = Flask(__name__)

# route register
app.register_blueprint(demo_controller, url_prefix='')
app.register_blueprint(aurin_controller, url_prefix='/api/aurin')
app.register_blueprint(twitter_controller, url_prefix='/api/twitter')

@app.errorhandler(404)
def handle404(err):
   return 'your request is wrong, please try again'

@app.errorhandler(500)
def handle404(err):
   return 'server data error, please contact the administrator'

#local test
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
