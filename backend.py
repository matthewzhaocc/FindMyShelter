import flask

import requests
import json
import string
import hashlib
import random
import base64

from mysqlControllerUser.controller import jsonStoreController
from mysqlcontrollerCompanyUser.companyController import companyController
from mysqlControllerShelter.shelterController import shelterController
app = flask.Flask(__name__)


userid = 0

@app.route('/',methods = ['GET'])
def rootPage():
    return flask.render_template('landing.html')

@app.route('/login', methods = ['POST'])
def login():
    userdata = {
        "usertype": flask.request.form['usertype'],
        "username": flask.request.form['username'],
        "password": hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest()
    }
    control = jsonStoreController()
    if userdata["usertype"] == 'org':
        control = companyController()
    ans = control.getPassword(userdata['username'])
   
    ree = {
        'usertype':ans[1],
        'loginstatus':str(ans[0]==userdata["password"]),
        'username':userdata['username']
    }
    res = flask.make_response(' ')
    res.set_cookie('info',base64.b64encode(str.encode(json.dumps(ree))))
    return res

@app.route('/register',methods = ['POST'])
def register():
    global userid
    if flask.request.method == 'POST':
        userid += 1
        controller = jsonStoreController()
        payload = {
            'usertype':flask.request.form['usertype'],
            'username':flask.request.form['username'],
            'password':hashlib.sha512(str.encode(flask.request.form['password'])).hexdigest(),
            'details':flask.request.form['details']
        }
        if payload['usertype'] == 'user':
            controller = jsonStoreController()
            payload['shelter']=' '
            controller.newUser(payload)
        else:
            controller = companyController()
            controller.newCompanyUser(payload)
        return ' '

@app.route('/newShelter', methods=['POST'])
def newShelter():
    if json.loads(base64.b64decode(str.encode(flask.request.cookies.get('info'))))['usertype'] == 'user':
        return ' '
    
    payload = {
        'Organization':json.loads(base64.b64decode(str.encode(flask.request.cookies.get('info'))))['username'],
        'name':flask.request.form['name'],
        'open':True,
        'capacity':flask.request.form['']
        }
    controller = shelterController()
    controller.newShelter(payload)
    return ' '

@app.route('/dashboard',methods=['GET'])
def companyDashboard():
    info = json.loads(base64.b64decode(flask.request.cookies.get('info')))
    controller = companyController()
    res = controller.getInfo(info['username'])
    print(res)
    details = json.loads(res[1])
    control = shelterController()

    return flask.render_template('organization.html', **{
        'username' : res[0],
        'phone': details['phone'],
        'address': details['address'],
        'email': details['email'],
        'shelters': control.getAllShelterFromCompany(res[0])
    })

@app.route('/search')
def searchengine():
    pass
app.run(host='0.0.0.0',port=5000,debug=True)