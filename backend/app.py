from flask import Flask

from controller.demo_controller import demo_controller
from controller.demo_restful_controller import demo_restful_controller

app = Flask(__name__)

# route register
app.register_blueprint(demo_controller, url_prefix='')
app.register_blueprint(demo_restful_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run()
