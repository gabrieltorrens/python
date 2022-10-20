import urllib.request
import json

def printResults(data):
    #print(data)
    responseJSON = json.loads(data) #string response to dictionary
    #print(responseJSON)
    if "title" in responseJSON["metadata"]:
        print(responseJSON["metadata"]["title"])

url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"
request = urllib.request.urlopen(url)
print("Request code is:", str(request.getcode())) #result code
data = request.read()
printResults(data)

