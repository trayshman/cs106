# CS106 Fall 2021
# Quiz 1
# Name: Ryan Jones

######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code

# Write code for the program shown on Slide 5 from September 9
# (VariablesExpressionsStatements.pdf).
# This program prompts the user to enter the number of students in the class
# and the number of professors in the class, then prints the total number of
# people in the class.
#
# Your output should be similar to that shown on the document for this quiz
# on theSpring.

# Write your code for Problem 1 here:
students=int(input('How many students are in the class? '))
professors=int(input('How many professors are in the class? '))
total=int(professors+students)
print('There are',total,'people in the class')


######################################################################
# Problem 2
print('\n\n***** Problem 2:') # Do not change this line of code

# Write code for a program that asks the user to enter an integer, then prints
# a message indicating whether or not that integer is divisible by 7.
#
# Your output should be similar to that shown on the document for this quiz
# on theSpring.

# Write your code for Problem 2 here:
x=int(input('Enter an integer '))
if x % 7 ==0:
    print(x,'is divisible by 7')
else:
    print(x,'is not divisible by 7')
    
