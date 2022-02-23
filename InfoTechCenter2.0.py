import random
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