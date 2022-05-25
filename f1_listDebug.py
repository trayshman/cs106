# Your name: Ryan Jones

# CS106 Fall 2021
# Final Exam Take Home Problem 1 (13 points)
# f1_listDebug.py: Correct the bugs in the code.

# INSTRUCTIONS: Correct the logic and/or semantic errors in two functions: fn1 and fn2.
# After the code is corrected the output from this program should match the sample output.
#
# Rules for corrections:
#   * You may only modify the lines marked with the "fix this line" comment.
#   * You may not add or delete lines of code.
#   * Recommended approach: Make a copy of the section of code, comment out the
#     original and make your changes to the copy. This allows you to easily see the
#     original function while you work on this problem.
#   * Tip: The errors are related to the concepts of lists.

############################################################
# TASK 1 (4 points)
# STUDENT MUST FIX THE ERRORS IN THIS FUNCTION
# Function name: fn1
# Function parameter:
#    list - a list of integers. This list is modified by the function.
# Returns: nothing (void function)
# Description:
# This function updates each item in the parameter list.
def fn1(x):
    for i in range(len(x)): # fix this line
        x[i] = x[i] * 3  # fix this line
# end of fn1


############################################################
# TASK 2 (9 points)
# STUDENT MUST FIX THE ERRORS IN THIS FUNCTION
# Function name: fn2
# Function parameter:
#    list - a list of integers. The function does not modify this list.
# Returns: A list where the value of each item is computed using the
#    corresponding item from the parameter list.
# Description:
# This function creates a new list where the value of each item in new list is
# the computed using the corresponding item in the parameter list.
def fn2(y):
    k = [] # fix this line
    for j in range(len(y)): # fix this line
        a = y[j] * 2 + y[j] * 3 # fix this line
        k.append(a)
    return k
# end of fn2


# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have corrected the functions above, your functions must work with the
# code that is provided below.

# Main part of program
listA = [13, 2, 11, 7, 8, 1, 6, 4, 12, 9, 14]
print('listA before calling fn1:', listA)

fn1(listA)
print('\nlistA after calling fn1:', listA)

listB = [4, 9, 3, 7, 2, 14, 6, 1]
print('\nlistB before calling fn2:', listB)

new_list = fn2(listB)
print('\nlistB after calling fn2:', listB)
print('new_list after calling fn2:', new_list)
