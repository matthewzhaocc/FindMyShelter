import requests
import json

class jsonStoreControllerLocation:
    def __init__(self):
        self.url = json.load(open('jsonStoreControllerLocation/config.json'))['jsonstoreURL']
    
    def newLocation(self, locationName, locationAddress, locationid, roomCount):
        payload = {
            'name':locationName,
            'address':locationAddress,
            'room':roomCount
        }
        requests.post(self.url+'/users/'+locationid, data=payload)
    
    def changeRoomCount(self,locationName, roomCount,):
        res = requests.put(url=self.url+'/users/'+id+'/room',data=strI)

    
    def getID(self,locationName)