import random

# Weather branch

def weather ():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather Function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your Alarm 30 minutes earlier based on the NWS forecast of",weatherAlert,":(")
        print("VRS will only allow your vehicle to go 30mph")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your Alarm 15 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your vehicle to go 15mph")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your vehicle to go 60mph")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your vehicle to go 70mph")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your Alarm 5 minutes earlier based on the NWS forecast of", weatherAlert, ":(")
        print("VRS will only allow your vehicle to go 60mph")
    else:
        print("\nWeather is",weatherAlert, "Let's GOOOOOOOOOOOO")
        print("VRS will alow your car to go 120MPH")

vehicleResponseSystem()