import json

from twilio.rest import Client

def loadJson(pathJson):
    """ Load json file and return a dictionary"""
    with open(pathJson, "r") as read_file:
        data = json.load(read_file)
    return data


#load json file with twilio settings
twilioSettings = loadJson("set.json")
#load json file with numbers and message to send
message = loadJson("message.json")
print(twilioSettings, message)

client = Client(twilioSettings['sid'], twilioSettings['auth'])
message = client.messages.create(body="kiubo ñeraaa puñala puñala >:v",
                                 from_=message['from'],
                                 to=message['to']['me'])
print(message.sid)
