# CS106 Fall 2021
# Final Exam Practice Problem B-6
# print_valid.py
# Uses regular expressions to validate the parentheses of a Python print statement.

import re

def check_prints(prints):

    # DO NOT MODIFY regex1
    # regex1: matches a valid print statement
    # Statement begins with the word 'print', the data to print is enclosed in parentheses
    regex1 = 'print\s*\(.*\)'

    # STUDENT MUST COMPLETE:
    # Write the three regular expressions as described below.
    # These regular expressions should result in program output that matches
    # the sample output shown on the instructions PDF.
    # Use regex1 given above to guide you in writing these three regular expressions.

    # regex2: matches a print statement with the error of missing a closing parenthesis
    regex2 = 'print\s*\([^)]*'

    # regex 3: matches a print statement with the error of missing an opening parenthesis
    regex3 = 'print\s*[^(]*\)'

    # regex4: matches a print statement with the error of no parentheses
    regex4 = 'print\s*[^(]*'


# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.
#
# You may assume the validation is always done in this order.

    for p in prints:
        if re.search(regex1, p):
            print(p, ' --- is valid')
        elif re.search(regex2, p):
            print(p, '--- missing closing parenthesis')
        elif re.search(regex3, p):
            print(p, '--- missing opening parenthesis')
        elif re.search(regex4, p):
            print(p, '--- missing parentheses around data to be printed')
        else:
            # Note: this error message should not print for the tests in this file
            print(p, '--- does not match a specific error')

# Main part of program
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.


valid_prints = ["print('abc', 123, 456)", "print(123)", "print()", "print     (123)"]
check_prints(valid_prints)
print()

error_prints = ["print 123", "print(123", "print 123)", "print 'abc', 123, 456", "print     ('abc', 123   ", "print      )", 'print', 'print(']
check_prints(error_prints)
