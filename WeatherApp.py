#Author: Ben Avery
#Date: 2-20-21

import json, urllib, urllib.request, time, logging

#"""
#//a "debugmode" variable, when true checks to see if dummy json data is available.
# #   If yes, load it, if no download the data and save it to disk.


#"""
def gettodaysforecast():
    curTime = time.localtime()
    if 3 < curTime.tm_hour < 15:
        nearesthour = 6
    else: nearesthour = 18
    rightnow = "{}-0{}-{}T{}:00:00-08:00".format(curTime.tm_year, curTime.tm_mon, curTime.tm_mday, nearesthour)
    defaultlocation =  json.loads('{ "long" : 48.769 , "lat" : -122.459}')
    todayforecast = getcurweather(defaultlocation)


    #TODO turn this into a function that takes in today forecast and returns the URL
    forecastRequest = urllib.request.urlopen(todayforecast["properties"]['forecast'])
    forecastData = json.load(forecastRequest)
    shortforecast = forecastData['properties']['periods'][0]['shortForecast']
    temperature = forecastData['properties']['periods'][0]['temperature']
    print("It is {} degrees and the weather is {}".format(temperature,shortforecast))


def getcurweather(address):
    weburl = "https://api.weather.gov/points/{},{}".format(address["long"], address["lat"])
    #print(weburl)
    currequest = urllib.request.urlopen(weburl)
#    print(currequest)
    curdata = json.load(currequest)
    logging.debug(curdata)
    return curdata

#...

def main():
    logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
    #open the url (to an HTTPResponse object), load the data into a json object.
    defaultcoords = '{ "long" : 48.769 , "lat" : -122.459}'
    coordjson = json.loads(defaultcoords)
    data = gettodaysforecast()

main()
