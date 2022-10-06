from email.mime import base
import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0012993441012'}

response = requests.get(baseUrl, params=parameters)
#print(response.url)
#print(response.text)

content = response.content
info = json.loads(content) #converts to dictionary

#print(type(info))
#print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

print(title)
print(brand)