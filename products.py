# CS106 Fall 2021
# Final Exam Practice Problem B-4
# products.py

# Task 1: read data from a file into a dictionary.
# Each line of the file contains the name of a product and a floating point number
# of the sales of that product. The file contains data from multiple sources
# and the product names are repeated multiple times in the file.
# The delimiter character is comma.
# The dictionary key is the product name, the value is the sales of that product.
# While reading the file, keep a sum of the sales of that product as the dictionary key.

fhand = open('sales.txt') # File handle for the input file

# Write your code for Task 1:
products=dict()

sumsales=0
for line in fhand:
    line=line.strip()
    things=line.split(',')
    products[things[0]]=things[1]
    sumsales+=float(things[1])
# NOTE: For Tasks 2 and 3, if you did not complete Task 1 you may use the following dictionary
stuff = {'qrs':23.45, 'abc':98.76, 'xyz': 76.54, 'pqr': 34.56, 'jkl': 87.65}

# Task 2: Print the items from the dictionary, sorted alphabetically by product name
# Write your code for Task 2:
key_list = list(products.keys())

key_list.sort() # Sort the list of keys

for k in key_list:
    # Print the key and its associated value from the dictionary
    print(k, products[k])

# Task 3: Find the product that has the maximum sum of sales (the value field
# in the dictionary). Print that product's name and sum of sales.
# Write your code for Task 3:
