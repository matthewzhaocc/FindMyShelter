import json
import requests
import mysql.connector
class jsonStoreController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            database='login',
            user='matthew',
            passwd='ABab12$$'
        )
        self.cursor = self.conn.cursor()
        self.newUserTemplate = 'INSERT INTO loginDatabase (username,password,usertype) VALUES (%s,%s,%s)'
        self.getPasswordTemplate = 'SELECT password,usertype FROM loginDatabase WHERE username=%s'

    def newUser(self,jsonPayload):
        val = (jsonPayload['username'],jsonPayload['password'],jsonPayload['usertype'])
        self.cursor.execute(self.newUserTemplate,val)
        self.conn.commit()
        self.conn.close()

    def getPassword(self,username):
        val = (username,)
        self.cursor.execute(self.getPasswordTemplate,val)
        return self.cursor.fetchone()
    