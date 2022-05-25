# CS106 Lab
# October 21, 2021
# Names and roles of group members: Recorder: Ryan Jones Organizer: Yuqian Sun

######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code
# Learning goals: Practice writing a function
#
# Write a function called get_int that has two parameters: an integer and a string.
# The function prints the string as the input prompt and validates that the user
# input is an integer and is greater than the function parameter.
# The function should use a loop to keep asking for user input until the user
# enters correct input, then the function returns this value. The function must
# handle any type of incorrect input (string, floating point number, integer
# less than or equal to the function parameter).
#
# See the document for this lab on theSpring for example output.

# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_int
# Function parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.

def get_int(lower,prompt):
    intflag=False
    while not intflag:
        x=input(prompt)
        try:
            x=int(x)
            if x > lower:
                intflag=True
        except:
            print('you must enter an integer')
    return(x)




# end of getInput function

# This code tests the get_int function
# Do not modify this test code. You may add more tests.
a = get_int(0, 'Enter an integer greater than zero: ') # Get input that is greater than 0
print('You entered the value:', a)

b = get_int(-100, 'Enter an integer greater than -100: ') # Get input that is greater than -100
print('You entered the value:', b)

######################################################################
# Problem 2
print('\n\n***** Problem 2:') # Do not change this line of code
# Learning goals: Practice writing a function
#
# Write a function called getFloat that has two parameters: a float and a string.
# The function asks the user to input a floating point number and validates that
# the user input is a floating point number and is greater than the function
# parameter. The function should use a loop to keep asking for user input until
# the user enters correct input, then the function returns this value. The
# function must handle any type of incorrect input (string, number that is less
# than or equal to the function parameter).
#
# See the exercises the document for this lab on theSpring for example output.

# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_float
# Function parameters:
#    float - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is a floating point number, and
# is greater than the lower bound.
def get_float(lower,prompt):
    floatflag=False
    while not floatflag:
        y=input(prompt)
        try:
            y=float(y)
            if y > lower:
                floatflag=True
        except:
            print('you must enter a number')
    return(y)


# end of getInput function

# Comment out this test code until you have written the get_float function.
# This code tests the get_float function
# Do not modify this test code. You may add more tests.
a = get_float(0.5, 'Enter a number greater than 0.5: ') # Get input that is greater than 0
print('You entered the value:', a)

b = get_float(100, 'Enter a number greater than 100: ') # Get input that is greater than 100
print('You entered the value:', b)

######################################################################
# Problem 3 (Based on Textbook Exercise 4.6)
print('\n\n***** Problem 3:') # Do not change this line of code
# Learning Goals: practice writing a function and calling the functions you wrote.
#
# Rewrite your pay computation program (Problem 2 from lab on February 12, and
# exercises 3.1 and 3.2 from the textbook). Recall that this problem asks the
# user to enter the number of hours worked and the pay rate. The pay is computed
# with 1.5 times the pay rate for hours worked above 40 hours.
#
# Requirements for this problem:
# 1) Create a function called computepay that has two parameters (hours and rate).
#    This function returns the computed pay. This function does NOT perform
#    any input or output. The body of this function is the code you wrote
#    on February 12 lab, without any input or output.
# 2) Write code that uses the function from Problem 1 to ask the user to enter
#    the hours worked (must be more than 0), and uses the function from Problem 2
#    to ask the user to enter the pay rate (must be more than 0). The code then
#    calls the compute pay function to get the pay, and then prints the employee's pay.

# STUDENT MUST WRITE THIS FUNCTION
# Function name: computepay
# Function parameters:
#    integer - number of hours worked
#    float - hourly pay rate
# Returns: the employee's pay for the week.
# Description:
# This function computes the employee's pay for the week. The employee earns
# overtime pay of 1.5 times the pay rate for any hours in excess of 40 hours.
def computepay(hours,wage):

    pay = wage * hours
    if hours>40:
        pay = (hours - 40) *  (wage * 1.5)
        pay = pay + (40*wage)
        return(pay)
    else:
        return(pay)


# end of computepay function

# STUDENT MUST WRITE CODE THAT USES THE FUNCTIONS
# Call the get_int function to get the hours worked from user input.
# Call the get_float function to get the pay rate from user input.
# Call the computepay function to calculate the pay for the week.
# Print the pay for the week.

a = get_int(0, 'enter hours worked:  ')
b = get_float(0, 'enter wage: ')

salary = computepay(a,b)
print(salary)

######################################################################
# Problem 4 - Bonus Problem (work on this if you finish the first three problems)
print('\n\n***** Problem 4:') # Do not change this line of code
# Learning goals: Practice writing a function
#
# Write a function called get_int_range that has three parameters: two integers and a string.
# The function prints the string as the input prompt and validates that the user
# input is an integer, is greater than the first parameter, and is less than the
# second parameter. The function should use a loop to keep asking for user input
# until the user enters correct input, then the function returns this value. The
# function must handle any type of incorrect input (string, floating point number,
# integer outside of the desired range).
#
# See the exercises the document for this lab on theSpring for example output.

# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_int_range
# Funtction parameters:
#    integer - lower bound
#    integer - upper bound
#    string - input prompt
# Returns: the validated user input
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, is greater than
# the lower bound, and is less than the upper bound.

def get_int_range(lower,upper,prompt):
    rangeflag=False
    while not rangeflag:
        x=input(prompt)
        try:
            x=int(x)
            if x>lower and x<upper:
                rangeflag=True
        except:
            print('you must enter an integer')
    return(x)

# end of get_int_range function

# Comment out this test code until you have written the get_int_range function.
# This code tests the get_int_range function
# Do not modify this test code. You may add more tests.
a = get_int_range(0, 100, 'Enter an integer between 0 and 100 (exclusive): ')
print('You entered the value:', a)

b = get_int_range(-100, 100, 'Enter an integer between -100 and 100 (exclusive): ')
print('You entered the value:', b)
