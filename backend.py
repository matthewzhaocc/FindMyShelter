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
        'usertype':userdata['usertype'],
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
    payload = {
        'Organization':(json.loads(base64.b64decode(str.encode(flask.request.cookies.get('info'))))['username']),
        'name':flask.request.form['name'],
        'open':True,
        'Capacity':flask.request.form['capacity'],
        'location':flask.request.form['location']
        }
    controller = shelterController()
    print(payload)
    controller.newShelter(payload)
    return flask.redirect(flask.url_for('companyDashboard'))

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

@app.route('/logout')
def logout():
    tres = flask.make_response(flask.redirect("/"))
    tres.set_cookie("info", " ")
    return tres


@app.route('/search')
def searchengine():
    controller = shelterController()
    allShelter = controller.getAllShelter()
    
    return flask.render_template('search.html',shelters=allShelter)

@app.route('/newReservations/<shelter>',methods = ['GET'])
def newReservations(shelter):
    num1 = flask.request.cookies.get('info')
    num2 = base64.b64decode(str.encode(num1))
    num3 = json.loads(num2)
    payload = {
        'name':shelter,
        'user':num3['username']
    }
    controller = shelterController()
    controller.delOneCap(payload['name'])
    controller = jsonStoreController()
    controller.changeShelter(payload['user'],payload['name'])
    return ' '
    
app.run(host='0.0.0.0',port=5000,debug=True)