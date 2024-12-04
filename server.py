from flask import Flask
from flask import request
import os
import sys

#Connect Controller definitions
fpath = os.path.join(os.path.dirname(__file__), 'controllers')
sys.path.append(fpath)
fpath = os.path.join(os.path.dirname(__file__), 'models')
sys.path.append(fpath)
from controllers import FruitController, SessionController

app = Flask(__name__, static_url_path='', static_folder='static')

#The Router section of our application conects routes to Contoller methods
app.add_url_rule('/', view_func=SessionController.login, methods = ['GET'])
app.add_url_rule('/index', view_func=SessionController.login, methods = ['GET'])
app.add_url_rule('/login', view_func=SessionController.login, methods = ['GET'])

app.add_url_rule('/fruit', view_func=FruitController.fruit, methods = ['POST', 'GET'])
app.add_url_rule('/fruit/<fruit_name>', view_func=FruitController.single_fruit, methods = ['GET'])

#Start the server
app.run(debug=True, port=5000)