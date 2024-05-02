from flask import Flask

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_world():
    return "<h1>Hello, my name is Mikita</h1>"