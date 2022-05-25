# fib.py
# Author: Christine F. Reilly
# Using recursion, calculate the Fibonnaci number at the specified position.

# Function name: fib_num
# Function parameter: The position in the Fibonnaci sequence
# Returns: The Fibonnaci number at the specified position
# Description:
# Using recursion, calculate the Fibonnaci number at the specified position.
def fib_num(pos):
    if pos == 0:
        # A base case. Fibonnaci number at position 0 is defined as 0
        fib = 0
    elif pos == 1:
        # A base case. Fibonnaci number at position 1 is defined as 1
        fib = 1
    else:
        # Recursive case. Recursively call the fib_num function to find the
        # Fibonnaci numbers at the previous two positions
        n2 = fib_num(pos - 2) # Fibonnaci number at two prior to this position
        n1 = fib_num(pos - 1) # Fibonnaci number at one prior to this position

        # Add Fibonnaci numbers at the prior two positions to get the
        # Fibonnaci nubmber for this position
        fib = n2 + n1
    # End of conditional structure
    return fib
# End of fib_num function

# Main part of program
p = int(input('At what position do you want to calculate the Fibonnaci number? '))
n = fib_num(p)
print('At position', p, 'the Fibonnaci number is', n)

# Try some larger positions and notice how long the program takes to run
# Use increments of 5 in the position number you try. By position 20 or 30
# you will probably notice that the program is running slower. By position 30
# to 40 you will probably notice that the program is much slower.
# If the program is taking too long to run you can end it.
# To stop a running program in the terminal, type the control key and the letter c
# key at the same time.
