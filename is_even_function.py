# is_even_function.py
# Author: Christine F. Reilly
# Example of writing and using a function

# is_even function
# Parameter x: an integer
# Returns True if the parameter is even, False otherwise
def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False
# End of is_even function

# Get an integer from user input, assume the user enters valid input
val = int(input('Enter an integer: '))

# Call the is_even function and save the return value in a variable
even = is_even(val)

# Print a message based on the function return value
if even == True:
    print(val, 'is even')
else:
    print(val, 'is odd')
