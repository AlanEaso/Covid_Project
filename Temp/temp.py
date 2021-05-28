import requests
import json

def createjson():
    res = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/chengannur.json?access_token=pk.eyJ1IjoiYWJoaWttcCIsImEiOiJja2phM2xjZDQ3N214MnFsYm9icWFidWRpIn0.xpSSYysroFrKHyZcTBFcVw");
    data = res.json();
    with open('data.json','w') as f:
        json.dump(data,f)

def readfromjson():
    with open('data.json') as f:
        data = json.load(f)
    print(data['features'][1]['center'])

def getCoords(place):
   res = requests.get("https://api.mapbox.com/geocoding/v5/mapbox.places/" + place + ".json?access_token=pk.eyJ1IjoiYWJoaWttcCIsImEiOiJja2phM2xjZDQ3N214MnFsYm9icWFidWRpIn0.xpSSYysroFrKHyZcTBFcVw");
   data = res.json()
   return data['features'][1]['center']
   #print(data['features'][1]['center'])

def writetoJSON(data, file):
    with open(file,'w') as f:
        json.dump(data,f)

def getDirections(start, end):
    url = "https://api.mapbox.com/directions/v5/mapbox/driving/"+str(start[0])+','+ str(start[1])+';'+str(end[0])+','+str(end[1])+"?alternatives=true&geometries=geojson&access_token=pk.eyJ1IjoiYWJoaWttcCIsImEiOiJja2phM2xjZDQ3N214MnFsYm9icWFidWRpIn0.xpSSYysroFrKHyZcTBFcVw"
    res = requests.get(url)
    data = res.json()
    writetoJSON(data,'directions.json')
    #print(data['routes'][0]['geometry'])

def getWaypoints():
    l=[]
    w = {}
    with open('directions.json') as f:
        data = json.load(f)
        #print(len(data['routes']))
        for i in range(len(data['routes'])):
            w["route_{}".format(i)] = data['routes'][0]['geometry']
        with open('waypoints.json','w') as file:
             json.dump(w, file)

start = getCoords('chengannur')
end = getCoords('kumbanad')

getDirections(start, end)
getWaypoints()


