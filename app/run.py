from flask import Flask, render_template
import requests

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/backend')
def get_data():
    return requests.get('http://backend.default:5200/msg/').content