import json
import requests

class jsonStoreController:
    def __init__(self):
        self.url = json.load(open('config.json'))['jsonstoreURL']

    def newUser(self,jsonPayload,id):
        requests.post(url=self.url+'/users/'+id,data=jsonPayload)
    
    def getUserPassword(self,username):
        res = requests.get(url=self.url+'/users?orderKey=username&filterValue='+username)
        return res.json['password']