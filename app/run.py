# from flask import Flask
# from flask_cors import CORS

# app = Flask(__name__, static_url_path='', static_folder='static')
# CORS(app)

# @app.route('/msg/')
# def home():
#    return {'msg': 'This is a message from flask backend.'}

from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/msg/')
def home():
   return render_template('home.html')