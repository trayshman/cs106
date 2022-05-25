# CS106 Lab
# September 16, 2021
# Names and roles of group members:

######################################################################
# Problem 1 (2 points)
print('***** Problem 1:') # Do not change this line of code

# In this problem you will fix the code and answer the two questions below.

# Question 1a: What happens when you run this 'buggy' code?
# Invalid if statement, else is never reached.

# Question 1b: What needs to be fixed in this 'buggy' code?
# You need to add "x=="
# Code to run then fix:
# When the value of x is 4 or 5 this code should print '4 or 5'
# With any other values of x this code should print 'other value'
# You may only edit the line of code that is marked as needing to be fixed.
# Assume the user always enters an integer (input is always valid).

x = int(input('Enter an integer: '))
if x == 4 or x== 5: # fix this line of code
    print('4 or 5')
else:
    print('other value')


######################################################################
# Problem 2 (Textbook Exercises 3.1 and 3.2) (5 points)
print('\n\n***** Problem 2:') # Do not change this line of code
#
# Rewrite your pay computation from last week (September 9, Problem 3) with
# two enhancements:
# a) Give the employee 1.5 times the hourly rate for hours worked above
# 40 hours.
# b) Use try and except so that your program handles non-numeric input
# gracefully by printing a message and setting that value to -1. Provide
# specific infhoursormation so the user knows which value was entered incorrectly.
#
# The hours worked is an int.
# The pay rate is a float.
#
# See the document for this lab on theSpring for example output.
#
# Note: make any corrections needed to your code from last week. Review the
# grade and feedback on theSpring for last week's group work.

# Write your code for Problem 2 here:
try:
    hours = int(input("ENTER NUMBER OF HOURS: "))
except ValueError:
    print("THAT VALUE IS NOT ACCEPTABLE. HOURS IS NOW EQUAL TO -1. ")
    hours = -1
try:
    salary = float(input("ENTER PAY PER HOUR: "))
except ValueError:
    print("THAT VALUE IS NOT ACCEPTABLE. HOURS IS NOW EQUAL TO -1. ")
    salary = -1
if hours> 40:
    salary*= 1.5
grossPay = round(hours * salary, 2)
print("YOUR PAY GROSS PAY IS $" + str(grossPay))

######################################################################
# Problem 3 (3 points)
print('\n\n***** Problem 3:') # Do not change this line of codeS
#
# Ask the user to input y or n (for yes or no) and save the user's input to a
# variable.
# Use conditional execution to verify the user entered y or entered n. If the
# user entered some other input, print a message and set the variable to 'n'.
# Print the value stored in the variable.
#
# See the document for this lab on theSpring for example output.
#
# Write your code for Problem 3 here
stuff = str(input("INPUT y OR n (for yes or no) ")
if stuff != "n" or stuff != "y":
    print("WRONG INPUT YOUR ANSWER HAS BEEN CHANGED TO n ")
    stuff = "n"
print(stuff)
