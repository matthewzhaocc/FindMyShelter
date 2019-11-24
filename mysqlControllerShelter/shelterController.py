import mysql.connector
import json
import math
class shelterController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='matthew',
            passwd='696969696969',
            database='shelter'
        )
        self.cursor = self.conn.cursor()
        
        self.newShelterTemplate = 'INSERT INTO shelterlocations (Organization,name,location,Capacity,open) VALUES (%s,%s,%s,%s,%s)'
        self.switchShelterStateTemplate = 'UPDATE shelterLocations open=%s WHERE name=%s'
        self.getStateTemplate = 'SELECT open FROM shelterLocations WHERE name=%s'
        self.getInfo = 'SELECT Organization,location,Capacity,open FROM shelterLocations WHERE=%s'
        self.capacityMinusOne = 'UPDATE shelterLocations Capacity = Capacity - 1 WHERE name=%s'
        self.capacityAddOne = 'UPDATE shelterLocations Capacity = Capacity + 1 WHERE name=%s'
        self.getAllShelterFromCompanyTem = 'SELECT name,location,Capacity,open FROM shelterLocations WHERE Organization=%s'
    def newShelter(self,jsonPayload):
        val = (jsonPayload['Organization'],jsonPayload['name'],jsonPayload['location'],jsonPayload['Capacity'],jsonPayload['open'])
        self.cursor.execute(self.newShelterTemplate,val)

        self.conn.commit()
    
    def delOneCap(self,name):
        val = (name.replace('\\', ''),)
        self.cursor.execute(self.capacityMinusOne,val)
        self.conn.commit()
        
    def switchShelterState(self,name,state):
            val = (name,not state)
            self.cursor.execute(self.switchShelterStateTemplate,val)
            self.conn.commit()

    def getState(self,name):
        val = (name,)
        self.cursor.execute(self.getStateTemplate,val)
        return self.cursor.fetchone()[0]
    
    def getInfo(self,username):
        val = (username,)
        self.cursor.execute(self.getInfo,val)
        res = self.cursor.fetchone()
        res = {
            'Organization':res[0],
            'location':res[1],
            'Capacity':res[2],
            'open':res[3]
        }
        return res
    
    def capacityChange(self,val):
        neg = False
        if val < 0:
            val = math.abs(val)
            neg = True
        for i in range(val):
            if neg:
                self.cursor.execute(self.capacityMinusOne)
            else:
                self.cursor.execute(self.capacityAddOne)
            self.conn.commit()
            self.conn.close()
    
    def getAllShelterFromCompany(self,Organization):
        val = (Organization,)
        self.cursor.execute(self.getAllShelterFromCompanyTem,val)
        res = self.cursor.fetchall()
        return res
    
    def shelterLength(self):
        self.cursor.execute('SELECT id FROM shelterLocations')
        return len(self.cursor.fetchall)
    
    def getAllShelter(self):
        self.cursor.execute('SELECT name,location,Capacity FROM shelterLocations')
        return self.cursor.fetchall()
    