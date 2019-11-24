import flask

import requests
import json
import string
import hashlib
import random

import pymongo

from jsonStoreControllerUser.controller import jsonStoreController

app = flask.Flask(__name__)

global userid

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
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest()
        }
        control = jsonStoreController()
        ans = control.getUser()
        res = {
            'usertype':ans['usertype'],
            'loginstatus':ans['password']==userdata['password'],
            'username':flask.request.form['uskername']
        }
        return flask.jsonify(res)

@app.route('/register',methods = ['GET','POST'])
def register():
    if flask.request.method == 'GET':
        return flask.render_template('register.html')
    if flask.request.method == 'POST':
        userid += 1
        controller = jsonStoreController()
        payload = {
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['username'])).hexdigest
        }
        controller.newUser(payload,userid)
        return flask.redirect(flask.url_for('/login'))

@app.route('/company/dashboard',methods=['GET','POST'])
def companyDashboard():
    if flask.request.method == 'GET':
        return flask.render_template('companydashboard.html')

@app.route('/user/dashboard',methods=['GET','POST'])
def userDashboard():
    if flask.request.method == 'POST':
        return flask.render_template('userdashboard.html')
app.run(host='0.0.0.0',port=5000,debug=True)