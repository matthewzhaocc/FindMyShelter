import flask

import requests
import json
import string
import hashlib
import random

import pymongo

app = flask.Flask(__name__)

userid = 0
@app.route('/',methods = ['GET'])
def rootPage():
    return flask.render_template('index.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    if flask.requests.method == 'GET':
        return flask.render_template('login.html')
    if flask.requests.method == 'POST':
        userdata = {
            'user':flask.requests.form['user'],
            'password':hashlib.sha512(str.encode(flask.requests.form['password'])).hexdigest()
        }

@app.route('/register',methods = ['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')

app.run(host='0.0.0.0',port=5000,debug=True)