# Your name: ryan

# CS106 Fall 2021
# Final Exam Take Home Problem 5 (9 points)
# f5_regex.py: Write regular expressions

# INSTRUCTIONS: Write the regular expressions as instructed below.
# After the code is completed the output from this program should match the sample output.


import re

def check_assgn(stmts):

    # assignment structure: left_side = right_side 

    # DO NOT MODIFY regex1
    # The first regular expression is provided as an example of how to write
    # regular expressions to match the assignment structure. Use this example
    # to assist you with writing the three regular expressions below.
    #
    # regex1: matches a valid assignment statement, defined as stated here.
    # left_side starts with letter then has zero or more letters, numbers, and
    #    underscore characters
    # right_side can be any characters other than =
    regex1 = '^[a-zA-Z][a-zA-Z0-9_]*\s*=[^=]+$'

    # regex2: matches an assignment statement with the error of starting with a
    #    character that is not a letter
    # 2 points: matches specified pattern
    # 1 points: does not match other than the specified pattern
    regex2 = '^[^a-zA-Z][a-zA-Z0-9_]*\s*=[^=]+$' # Write this regular expression

    # regex3: matches an assignment statement with the error of containing = in
    #    the right_side
    # 2 points: matches specified pattern
    # 1 points: does not match other than the specified pattern
    regex3 = '^[a-zA-Z][a-zA-Z0-9_]*\s*=[=]+$' # Write this regular expression

    # regex4: matches an assignment statment with the error of the left_side
    # containing invalid characters
    # 2 points: matches specified pattern
    # 1 points: does not match other than the specified pattern
    regex4 = '^[INVALID CHARECTERS]]*\s*=[^=]+$' # Write this regular expression
#WHAT ARE INVALID CHARACTERS
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.

    for s in stmts:
        if re.search(regex1, s):
            print('is valid ---', s)
        elif re.search(regex2, s):
             print('left side does not start with letter ---', s)
        elif re.search(regex3, s):
             print('right side contains = ---', s)
        elif re.search(regex4, s):
             print('left side contains invalid caracters ---', s)
        else:
            print('does not match a specific error ---', s)

# Main part of program
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.

print('**** Test 1: matches regex1 ****')
valid_assgn = ['x = 5', 'x=5', 'x     =       5', 'my_var = func(a, b, c)', 'My123 = x + y / z', 'AnotherFunVar =123+(456*789)']
check_assgn(valid_assgn)
print()

print('**** Test 2: matches regex2 ****')
error_assgn1 = ['78abc = x', '$cost = 456.78', "(myvar = 'hello')"]
check_assgn(error_assgn1)
print()

print('**** Test 3: matches regex3 ****')
error_assgn2 = ['x = y + z = abc', 'x=y=z']
check_assgn(error_assgn2)
print()

print('**** Test 4: matches regex4 ****')
error_assgn3 = ['x+y=5', 'a + 5 = x', 'a-b-c = 123', 'my#1 = 1']
check_assgn(error_assgn3)
print()

print('**** Test 5: does not match any of the reglar expressions ****')
error_assgn4 = ['abc', 'abc123', 'x =', '= 123']
check_assgn(error_assgn4)
print()
