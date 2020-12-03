from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/dic')
def dic():
    return {'noise':'Hello, World!'}

@app.route('/')
def index():
    return 'Index Page'

from markupsafe import escape

@app.route('/test', methods=['POST'])
def json():

    req = request.get_json()

    print(type(req))
    print(req)

    return "Thanks"