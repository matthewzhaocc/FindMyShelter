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
            passwd='696969696969'
        )
        self.cursor = self.conn.cursor()
        self.newUserTemplate = 'INSERT INTO loginDatabase (username,password,usertype,shelter) VALUES (%s,%s,%s,%s)'
        self.getPasswordTemplate = 'SELECT password,usertype FROM loginDatabase WHERE username=%s'
        self.changeShelter = 'UPDATE shelter SET shelter=%s WHERE username=%s'

    def newUser(self,jsonPayload):
        val = (jsonPayload['username'],jsonPayload['password'],jsonPayload['usertype'],jsonPayload['shelter'])
        self.cursor.execute(self.newUserTemplate,val)
        self.conn.commit()

    def getPassword(self,username):
        val = (username,)
        self.cursor.execute(self.getPasswordTemplate,val)
        return self.cursor.fetchone()
    
    def newShelter(self,username,sheltername):
        val=(sheltername,username)
        self.cursor.execute(self.changeShelter,val)
        self.conn.commit()