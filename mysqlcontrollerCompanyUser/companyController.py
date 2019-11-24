import mysql.connector

import requests
import json

class companyController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='0.0.0.0',
            user='matthew',
            database='companyuser',
            passwd='ABab12$$'
        )
        self.newCompanyUserTemplate = 'INSERT INTO companyUserDatabase (username,password,usertype,details) VALUES (%s,%s,%s,%s)'
        self.cursor = self.conn.cursor()
    def newCompanyUser(self,jsonPayload):
        val = (jsonPayload['username'],jsonPayload['password'],jsonPayload['usertype'],jsonPayload['details'])
        self.cursor.execute(self.newCompanyUserTemplate,val)
        self.conn.commit()
        self.conn.close()
    
    
