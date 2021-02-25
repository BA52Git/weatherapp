#Author: Ben Avery
#Date: 2-20-21

import json, urllib, urllib.request, time, logging


#Load the JSON file for a particular set of GPS coordinates that will be used to derive weather info for the other functions
def getweatherfromcoords(gpscoords):
    weburl = "https://api.weather.gov/points/{},{}".format(gpscoords["long"], gpscoords["lat"])
    logging.debug(weburl)
    currequest = urllib.request.urlopen(weburl)
    curdata = json.load(currequest)
    logging.debug(curdata)
    return curdata

#"forecast" is one of the JSON files linked from the weather JSON that was retrieved by getweatherfromcoords.  The purpose
# of this function is to retrieve individual components of the forecast.
def getforecastdata(weatherdata,forecasttype,when):
    
    forecastRequest = urllib.request.urlopen(weatherdata["properties"]['forecast'])
    forecastData = json.load(forecastRequest)
    forecastresponse = forecastData['properties']['periods'][when][forecasttype]
    return forecastresponse


#returns the short forecast data.  This function is depreciated now that getforecastdata will return an individual element based on
#  what gets pased in 'forecasttype'
def shortforecast(weatherdata,when):
    shortforecast = getforecastdata(weatherdata,'shortForecast',when)
    return shortforecast

#depreciated similar to shortforecast()
def gettemperature(weatherdata,when):
    temperatureresponse = getforecastdata(weatherdata,'temperature',when)
    return temperatureresponse

#Since there are two components to wind, this function is worth keeping for ease of use
def windinfo(weatherdata,when):
    windspeed = getforecastdata(weatherdata,'windSpeed',when)
    winddirection = getforecastdata(weatherdata,'windDirection',when)
    return {'Wind Speed' : windspeed, 'Wind Direction' : winddirection}

#A command line interface method for the user to retrieve different types of forecast data.
#TODO change "inputs" to "forecast inputs" and create inputs for other pages, not just the information from getforecastdata()
def userinputrequest(weatherdata,when):
    inputs = {'temp' : 'temperature', 'wind' : 'windinfo', 'short' : 'shortForecast', 'long' : 'detailedForecast'}
    usersays = 'help'
    timeoutcount = 0
    while((usersays != 'exit') and (timeoutcount < 5)):
        usersays = input ("What kind of weather would you like to know about?")
        if usersays in inputs:
            if usersays == 'wind':
                response = windinfo(weatherdata, when)
                for d in response:
                    print(d + ": " + response[d], end = ' ')
                    print()
            else:
                response = getforecastdata(weatherdata,inputs[usersays],when)
                print(inputs[usersays] + ": " + str(response))
        else:
            print('please choose from the following options:')
            for d in inputs:
                print(d)
    

#...

def main():
    logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')

# TODO: Add an args line for coordinates from the commandline.  In the future, this can be an address.

    defaultcoords = '{ "long" : 48.75 , "lat" : -122.5}'
    rightnow = 0x00
    
    #open the url (to an HTTPResponse object), load the data into a json object.
    coordjson = json.loads(defaultcoords)
    weatherdata = getweatherfromcoords(coordjson)
    
    shortfore = shortforecast(weatherdata,rightnow)
    print("The short forecast is {}.".format(shortfore))
    windfore = windinfo(weatherdata,rightnow)
    for d in windfore:
        print(d + ": " + str(windfore[d]),end=' ')
    print()
    print()
    userinputrequest(weatherdata, rightnow)
    



main()
