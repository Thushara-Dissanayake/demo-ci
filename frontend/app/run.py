from flask import Flask, render_template
import requests

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/backend')
def get_data():
    return requests.get('http://backend:5200/msg/', headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}).content