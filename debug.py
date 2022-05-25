# CS106 Fall 2021
# Exam 1 Practice Problem
# debug.py: Correct the bugs in the code.

# INSTRUCTIONS: Correct the bugs in the four tasks in this program. Only
# modify the lines of code that are marked as needing to be corrected.
# You may enter different variable values for testing.

# Task 1: Add the values stored in variables a and b, store the result in
# variable c
a = 1
b = 2
c = a + b  # Correct this line of code


# Task 2: Print the value that is stored in variable c (the variable from Task 1)
print(c) # Correct this line of code


# Task 3: The value True should print when the variable m does NOT have a value
# between 1 and 99. Test your code with different values of m
m = -45 # Test with different values of m
print(m >= 0 or m < 100) # Correct this line of code


# Task 4: The message "y is in the middle" should print when the value of y is
# in between the values of x and z. Otherwise, the message "y is not in the middle"
# should print.
# Test with different values of x, y, and z.
x = 78
y = 43
z = 123
if x < y or y >= z: # Correct this line of code
    print('y is in the middle')
else:
    print('y is not in the middle')
