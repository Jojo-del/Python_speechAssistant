import json, requests
from pprint import pprint
from time import sleep

parameter= dict()
"""
print('123'=='321')
for i in range(0,350):
    response = requests.get(url,parameter)
    data = response.json()
    print(str(i)+ '. --- '+data["bpi"]["EUR"]["rate"])
    sleep(5)

print('done')
"""
#pprint(data, indent= 5)

class Bitcoin():
    def __init__(self, url= 'http://api.coindesk.com/v1/bpi/currentprice.json',parameter= dict()):
        self.url = url
        self.parameter= parameter

    def getResponse(self):
        response = requests.get(self.url, self.parameter)
        return response.json()

    def getEURBitcoins(self):
        data= self.getResponse()
        return data['bpi']['EUR']['rate']

    def getUSDBitcoins(self):
        data = self.getResponse()
        return data['bpi']['USD']['rate']

    def getTime(self):
        data= self.getResponse()
        return data['time']['updated']



