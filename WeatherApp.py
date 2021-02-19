
import json, urllib, urllib.request

#"""
#//a "debugmode" variable, when true checks to see if dummy json data is available.  If yes, load it, if no download the data and save it to disk.


#"""

jsonfile = open('jsonForecast.txt','w')

#...
jsonfile.close()

#open the url (to an HTTPResponse object), load the data into a json object.
request = urllib.request.urlopen("https://api.weather.gov/points/48.76977025604445,-122.45939985854866") 
data = json.load(request)

#open the forecast url from the previous webpage and load it into the forecastData json object for dissection
forecastRequest = urllib.request.urlopen(data["properties"]['forecast'])
forecastData = json.load(forecastRequest)
print(forecastData['properties']['periods'][0]['shortForecast'])