# To develop, run this command
# flask --app server.py --debug run
from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return "Hello!"

@app.get('/bye')
def index():
    return "bye!"