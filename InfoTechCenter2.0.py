import random
# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)
    return currentGasLevel

gasLevelGauge()

# create IF-ELIF-ELSE statements using Comparative Operators to display gas level messages
def gaslevelAlert():
    if gasLevelGauge() == "Empty":
        print("        ***WARNING***\n you have run out of gas\nCalling Emergency Contact")


gaslevelAlert()