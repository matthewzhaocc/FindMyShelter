import mysql.connector

import requests
import json

class companyController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='matthew',
            database='login',
            passwd='ABab12$$'
        )
        self.newCompanyUserTemplate = 'INSERT INTO companyUserDatabase (username,password,usertype,details) VALUES (%s,%s,%s,%s)'
        self.getUserTemplate = 'SELECT password, usertype FROM companyUserDatabase WHERE username = %s'
        self.getInfoTemplate = 'SELECT username,details FROM companyUserDatabase WHERE username = %s'
        self.cursor = self.conn.cursor()
    def newCompanyUser(self,jsonPayload):
        val = (jsonPayload['username'],jsonPayload['password'],jsonPayload['usertype'],jsonPayload['details'])
        self.cursor.execute(self.newCompanyUserTemplate,val)
        self.conn.commit()
        self.conn.close()
    def getPassword(self,username):
        val = (username,)
        self.cursor.execute(self.getUserTemplate,val)
        res = self.cursor.fetchone()
        return res
    
    def getInfo(self,username):
        val = (username,)
        self.cursor.execute(self.getInfoTemplate,val)
        return self.cursor.fetchone()

