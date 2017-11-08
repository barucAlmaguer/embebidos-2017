from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainpage():
    return "hola mundo"

@app.route('/log/<int:value>')
def logging(value):
    return value
