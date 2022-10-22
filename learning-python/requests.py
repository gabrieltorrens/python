import urllib.request
import json

def printResults(data):
    #print(data)
    responseJSON = json.loads(data) #string response to dictionary
    #print(responseJSON)
    if "title" in responseJSON["metadata"]:
        print(responseJSON["metadata"]["title"]) #value in nested dictionary
    
    count = responseJSON["metadata"]["count"]
    print("Events recorded:", count)

    #location of each
    for i in responseJSON["features"]:
        print(i["properties"]["place"])
        print("------------")

    #print if mag > 4
    for i in responseJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print(i["properties"]["place"])
            print("------------")
    
    #print if felt
    for i in responseJSON["features"]:
        if i["properties"]["felt"] != None:
            feltReports = i["properties"]["felt"]
            print(i["properties"]["place"], "felt by", feltReports, "people")

#get response
url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
request = urllib.request.urlopen(url)
print("Request code is:", str(request.getcode())) #result code
if (request.getcode() == 200):
    data = request.read()
    printResults(data)
else:
    print("Error getting data:", request.getcode())
