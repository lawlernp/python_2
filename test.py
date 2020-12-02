from flask import Flask, request
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'

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