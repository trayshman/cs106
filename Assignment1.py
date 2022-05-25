#Assignment1.py
#Ryan Jones
#This program calculates how much fuel a trip uses, the total fuel cost, and how much each traveler should pay

travelers=int(input('How many travelers are there? '))
#Gets variable for amount of travelers
miles=int(input('How many miles did you travel? '))
#Gets variable for how many miles traveled
fuelCost=float(input('What is the cost per gallon of fuel? $'))
#Gets variable for the cost per gallon of fuel
mpg=int(input('How many miles per gallon does the vehicle average? '))
#Gets variable for the miles per gallon rate of the car on average

tripUse=float(miles/mpg)
#Calculates how many gallons of fuel the trip used by dividing the amount of miles traveled by the mpg
print('The trip used '+str(tripUse)+' gallons of fuel')

totalFuel=float(tripUse*fuelCost)
#Calculates the total cost of the fuel by multiplying the amount of fuel the trip used by the cost per gallon
print('The total fuel cost was $'+str(totalFuel))

travelerContribute=float(totalFuel/travelers)
#Calculates how much each traveler should pay by dividing the total cost of the fuel by the amount of travelers
print('Each traveler should contribute $'+str(travelerContribute))
