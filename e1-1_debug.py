# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 1 Take Home Problem 1 (20 points)
# e1-1_debug.py: Correct the bugs in the code.

# INSTRUCTIONS: Correct the bugs in the three tasks in this program. Only
# modify the lines of code that are marked as buggy.

# Task 1 (5 points): Add the values stored in variables a and b, then divide
# that result by the value stored in variable c. Store the result in variable d.
# For the values provided for variables a, b, and c; variable d should have
# a value of 34.8
a = 98
b = 76
c = 5
d = (a + b) / c # Correct this line of code


# Task 2 (5 points): Print the value that is stored in variable d (the variable from Task 1)
print(d) # Correct this line of code


# Task 3 (10 points): Under the following conditions this code should print the
# value True:
#    When the variable m is larger than zero, and
#    When either variable j or variable k is larger than zero
# Under any other conditions, this code should print the value False.
# Example: when j is -3, k is 6, and m is 10: prints True
# Example: when j is -3, k is -6, and m is 10: prints False
# Example: when j is 3, k is 6, and m is 10: prints True
# Example: when j is -3, k is 6, and m is -10: prints False
# Example: when j is -3, k is -6, and m is -10: prints False
# Example: when j is 3, k is 6, and m is -10: prints False
# Test with different values of j, k, and m
j = 3
k = 6
m = 10
print(m > 0 and (j>0 or k > 0)) # Correct this line of code
