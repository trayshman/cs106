# CS106 Fall 2021
# Quiz 2
# Name: Ryan Jones

# The comments provide an outline of the code you need to write. Write your code
# for each action under the comment that describes that action.

# import the math library
import math

# Ask the user to enter the diameter of a circle (an integer)
diam=input('Enter the diameter of a circle: ')
# Validate that the user enters an integer.
# If the user does not enter an integer, set the value of the diameter to 1 and
# print a message.
try:
    x=int(diam)
except:
    print('Not the correct value, setting diameter to 1')
    diam=1


# Calculate the circumfrence of the circle (pi x diameter )
# You must use the value of pi from the Python math library
circum=math.pi*int(diam)



# Calculate the area of the circle
# area = pi x radius squared
# where radius is half of the diameter
# You must use the value of pi from the Python math library
circRadi=float(diam)/2
circArea=math.pi*(circRadi**2)


# Print the circumfrence and the area
# You must use one print statement to print both values
print('a circle with a diameter of',diam,'has a circumference of',circum,'and an area of',circArea)
