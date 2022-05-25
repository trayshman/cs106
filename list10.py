# CS106 Fall 2021
# Final Exam Practice Problem B-1

# list10.py: The function contains logic and/or semantic errors. Correct these
# errors so that the program output matches the sample output. Rules for corrections:
#   * You may modify one or more lines of code in the function.
#   * You may not add or delete lines of code.
#   * You may not change the function header.
#   * Recommended approach: Make a copy of the function, comment out the original
#     and make your changes to the copy. This allows you to easily see the
#     original function while you work on this problem.
#   * Tip: The errors are related to the concepts of lists and how data flows to
#     and from a function.

############################################################
# STUDENT MUST FIX THE ERRORS IN THIS FUNCTION
# EVERY LINE OF CODE IN THE FUNCTION BODY CONTAINS ERRORS
# Function name: set10
# Function parameter:
#    list - a list of integers. The function does not modify this list.
# Returns: A list of integers that is a modified copy of the parameter, such that
# any value in the parameter list that is greater than 10 is set to 10 in the
# returned list.
# Description:
# This creates a copy of the parameter list, and sets any value greater than 10
# in the new list to 10.
def set10(vals):
    new_vals = vals.copy()
    for v in range(len(new_vals)):
        if new_vals[v] > 10:
            new_vals[v] = 10
    # End of loop through list
    return new_vals
# End of set10 function

# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have fixed the function above, your function must work with the
# code that is provided below.

# Main part of program
num1 = [8, 7, 23, 30, 9, 19, 15, 13, 1, 7]
print('before calling set10_v2 num1 =', num1)
num2 = set10(num1)
print('after calling set10_v2 num1 = ', num1)
print('after calling set10_v2 num2 = ', num2)
