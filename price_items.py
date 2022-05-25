# price_items.py
# Author: Christine F. Reilly
# Given the price for some quantity of an item, calculates the price for the
# number of that item the user wishes to purchase.
# This is Problem 4 from September 9 lab group work, with the modification
# of output formatting

# Obtain information from user input
# Assume the user enters valid data
price = float(input('What is the given price? $'))
quant = int(input('For how many items? '))
purch = int(input('How many would you like to purchase? '))

# calculate the price for the quantity the user wishes to purchase
total = (price / quant) * purch

# This was the output on the Feb 5 lab
print(purch, 'of the product costs $' + str(total))

# Use printf formatting for the output
# %d is placeholder for an int
# %f is placeholder for float in decimal format
# Specify exactly two numbers to the right of the decimal point: %.2f
print('%d of the product costs $%.2f' % (purch, total))
