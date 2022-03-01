# Code NAme - Hornet

# Import libraries here
from time import sleep #Print to one line with time delay between prints

import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)
import random

# Welcome Branch

print(Fore.BLUE + "Welcome to Hornets InfoTechCenter\n")

sleep(1)

print(Fore.BLUE + "Hornet's Operating System Booting Up\n")

sleep(1)

# Gas Branch

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#variable calls the value of gaslevelGauge Function
gasLevelIndicator = gasLevelGauge()

# create IF-ELIF-ELSE statements using Comparative Operators to display gas level messages
def gaslevelAlert():
    gasStations = ["Shell","BP","Circle K","Speedway","Marathon","Love s","Meijer","Cosctco","Sunoco"]
    miles = round(random.uniform(1,25),1)
    if gasLevelGauge() == "Empty":
        print("        ***WARNING***\n you have run out of gas\nCalling Emergency Contact")
    elif gasLevelIndicator =="Low":
        print("***WARNING***\nYour gas tank is extremely LOW\nthe closest gasoline station is " + random.choice(gasStations) + " which is " + str(miles) + " miles away!")
    elif gasLevelIndicator =="Quarter Tank":
        print("You are on a QUARTER TANK of gas\nstart planning a visit to the gas station!!!")
    elif gasLevelIndicator == "Half Tank":
        print("you have a HALF TANK of gas\nyou have 125 more miles to empty!!!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You have THREE QUARTER TANK of gas\nYou hve 205 more miles til empty!!!")
    else:
        print("You have a FULL TANK of gas, Congratulations. \nYou have 310 more miels to empty!!!!")


gaslevelAlert()

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