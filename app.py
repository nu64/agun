from flask import flask

app = Flask (__name__)


@app.route ('/')
def index():
    return 'Hello world!'

@app.route ('/about')
def about ():
    return 'Saya agun'