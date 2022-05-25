# CS106 Lab
# November 18, 2021
# Names and roles of group members: Recorder: Ryan Jones, Organizer: Yuqian Sun


######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code
# Learning goals: Practice writing a recursive function.
#
# WRITE THIS FUNCTION
# Function name: rev_str
# Function parameter:
#    string - the string to reverse
# Returns: the string in reverse
# Description:
# Using recursion, this function returns the parameter string in reverse.
#
# Tips for writing this recursive function:
#   - Base case: empty string
#   - Recursive case: call this function with a parameter that has one less letter
#     (remove the first letter from the string, then recursively call the function).
#     When the recursive call returns, append the first letter of this string to the return string.
#   - See the reverse_input.py example program from class for a similar function.
#
# Write your code here for the rev_str function:
def rev_str(strung):
    if strung == '':
        return strung
    else:
        nstrung=strung[1:]
        a=rev_str(nstrung)
        return a+strung[0]




# main part of code for Problem 1
# Do not modify this code
s1 = 'ant'
s2 = 'caterpillar'
s3 = 'z'
s4 = ''

rs1 = rev_str(s1)
print(s1, 'reversed is', rs1)
print()

rs2 = rev_str(s2)
print(s2, 'reversed is', rs2)
print()

rs3 = rev_str(s3)
print(s3, 'reversed is', rs3)
print()

rs4 = rev_str(s4)
print(s4, 'reversed is', rs4)

######################################################################
# Problem 2
print('\n***** Problem 2:') # Do not change this line of code
# This is Exercise 6.2 from the textbook.
# Learning goals: Practice writing a recursive function.
#
# WRITE THIS FUNCTION
# Function name: rec_sum
# Function parameter:
#    int - The value to sum up to
# Returns: the sum of integers from 1 up to the parameter value.
# Description:
# Using recursion, this function sums all the integers from 1 up to the parameter
# value. The program may not use a loop. Rather, it must use recursion to carry
# out the summing process.
#
# Tips for writing this recursive function:
#   - Identify the base case: for what parameter value is the problem trivial to solve?
#   - In the recursive case, how do you move the problem closer to the base case?
#   - See the fib.py example program from class for a similar problem.
#
# Write your code here for the rec_sum function:

def rec_sum(num):
    if num == 1:
        return 1

    else:
        num2=num-1
        num3=rec_sum(num2)
        return num3+num



# main part of code for Problem 2
# Do not modify this code
n = int(input('Enter a positive integer: '))
r = rec_sum(n)
print('Result:', r)
