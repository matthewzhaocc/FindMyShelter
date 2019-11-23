import json
from twilio.rest import Client

class smsController:
    def __init__(self):
        conf = json.load(open('sms/config.json'))
        print(json.dumps(conf))
        self.smsClient = Client(conf['account_sid'],conf['auth_token'])
    def send(self,content,to):
        return self.smsClient.messages.create(**{
                "body": content,
                "from_": '+19733556792',
                "to": to
        }).sid
smsController().send('ur gay as fuk','+19256605447')