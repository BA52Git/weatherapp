
import json, urllib, urllib.request, datetime

#"""
#//a "debugmode" variable, when true checks to see if dummy json data is available.  If yes, load it, if no download the data and save it to disk.


#"""
def gettodaysforecast():
    curtime = datetime.time()
    if 3 < curtime.tm_hour < 15:
        curtime.tm_hour = 6
    else: curtime.tm_hour = 18
    rightnow = "{}-0{}-{}T{}:00:00-08:00".format(curTime.tm_year, curTime.tm_mon, curTime.tm_mday, curTime.tm_hour)
    todayforecast = getcurweather(('48.769', '-122.459'))

def getcurweather(address):
    weburl = "https://api.weather.gov/points/{},{}".format(address["long"], address["lat"])
    print(weburl)
    currequest = urllib.request.urlopen(weburl)
    curdata = json.loads(currequest)
    print(curdata)
    return curdata

#...

def main():
    #open the url (to an HTTPResponse object), load the data into a json object.
    defaultcoords = '{ "long" : 48.769 , "lat" : -122.459}'
    coordjson = json.loads(defaultcoords)
    data = getcurweather(coordjson)
    # request = urllib.request.urlopen("https://api.weather.gov/points/48.76977025604445,-122.45939985854866")
    # data = json.load(request)

    #open the forecast url from the previous webpage and load it into the forecastData json object for dissection
    forecastRequest = urllib.request.urlopen(data["properties"]['forecast'])
    forecastData = json.load(forecastRequest)
    print(forecastData['properties']['periods'][0]['shortForecast'])


main()
