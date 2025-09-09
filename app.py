from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello from Flask on PythonAnywhere!</h2>"

@app.route('/process')
def process():
    return "<p>Processing done ✅</p>"
