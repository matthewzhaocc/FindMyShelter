import mysql.connector
import json

class shelterController:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='matthew',
            passwd='ABab12$$',
            database='shelter'
        )