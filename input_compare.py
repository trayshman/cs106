# CS106
# Author: Christine F. Reilly
# Three versions of a function that gets and validates a value from user input.
# The purpose of this example code is to demonstrate the best style solution
# using the input variable as the loop control variable.

# Solution 1: The best style solution. Uses the input variable as the loop
# control variable. Every iteration of the loop performs one comparison.
# YOU SHOULD USE THIS AS YOUR get_int FUNCTION IN PROGRAMMING ASSSIGNMENT 6.
# Make modifications to this function for your get_int_range function.
#
# Function name: get_int_best
# Function parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.
def get_int_best(lower, prompt):
    x = lower
    while x <= lower:
        try:
            x = int(input(prompt))
        except:
            print('You must enter an integer.')
    #end of loop
    return x
# end of get_int_best function

# Solution 2: An acceptable style solution. Initializes the loop control variable
# to None, then includes a comparison with None in the loop condition.
# Every iteration of the loop performs two comparisons, both in the loop condition.
#
# Function name: get_int_good
# Function parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.
def get_int_good(lower, prompt):
    x = None
    while x is None or x <= lower:
        try:
            x = int(input(prompt))
        except:
            print('You must enter an integer.')
    #end of loop
    return x
# end of get_int_good function


# Solution 3: A poor style solution. Initializes the loop control variable to
# None, then resets the loop control variable to None if the user input is
# outside of the desired range. Every iteration of the loop performs two
# comparisons. Re-setting x to None after getting an input value outside of
# the desired range could lead to confusion when someone else reads the code.
#
# Function name: get_int_poor
# Function parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.
def get_int_poor(lower, prompt):
    x = None
    while x is None:
        try:
            x = int(input(prompt))
            # If we reach this point, x is an integer
            if x < lower:
                # the input is not within the valid range.
                # re-set x to None so the loop will run again.
                x = None
        except:
            print('You must enter an integer.')
    #end of loop
    return x
# end of get_int_poor function

# Solution 3: Perhaps the worst style solution. Uses a boolean value for loop
# control. Every iteration of the loop performs two comparisons. This solution
# requires an additional Boolean variable for loop control.
#
# Function name: get_int_bad
# Function parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input.
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.
def get_int_bad(lower, prompt):
    done = False
    while not(done):
        try:
            x = int(input(prompt))
            # If we reach this point, x is an integer
            if x >= lower:
                # The input is within the valid range.
                # Set done to True so loop will end.
                done = True
        except:
            print('You must enter an integer.')
    #end of loop
    return x
# end of get_int_bad function

# Main part of the program
# Test the functions. They all work the same.
a = get_int_best(0, 'Enter an integer greater than zero: ') # Get input that is greater than 0
print('You entered the value:', a)
print()

a = get_int_good(0, 'Enter an integer greater than zero: ') # Get input that is greater than 0
print('You entered the value:', a)
print()

a = get_int_poor(0, 'Enter an integer greater than zero: ') # Get input that is greater than 0
print('You entered the value:', a)
print()

a = get_int_bad(0, 'Enter an integer greater than zero: ') # Get input that is greater than 0
print('You entered the value:', a)
print()
