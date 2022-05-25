# CS106 Fall 2021
# Final Exam Practice Problem B-5
# odds.py

############################################################
# STUDENT MUST COMPLETE THIS FUNCTION
# Function name: odd_count
# Function parameter:
#    list - A list of integers
# Returns: The count of the number of odd numbers in the list
# Description:
# This function uses recursion to traverse a list of integers. When an odd integer
# is encountered, it is printed. The function returns the count of the number of
# odd integers in the list.
#
# Your task: Add to and modify the code in this function so that the function
# returns the count of odd numbers. You must use a recursive process for counting
# the number of odd numbers in the list.
#
# Tip: this problem can be solved by adding one line of code and modifying
# two lines of code.
def odd_count(values):

    count = 0 # Variable to use as part of counting odd numbers

    # Print odd numbers only
    if values[0] % 2 != 0:
        print(values[0])
        count = 1

    # Recursive part of function
    if len(values) == 1:
        # Base case: processing the last item in the list
        return count
    else:
        # Recursive case: call this function with a list where the first item
        # is removed. This moves the work down the list.
        ret = odd_count(values[1:])
        return count+ret

# end of odd_count function


# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.

# Main part of program

listA = [47, 41, 24, 43, 46, 16, 76, 63, 41, 46]

print('Odd numbers in listA:')
odds = odd_count(listA)
print('List A has', odds, 'odd numbers')

print()
listB = [32, 16, 128, 1024, 512, 2048, 8, 256]
print('Odd numbers in listB:')
odds = odd_count(listB)
print('List B has', odds, 'odd numbers')

print()
listC = [13, 33, 7, 29, 45]
print('Odd numbers in listC:')
odds = odd_count(listC)
print('List C has', odds, 'odd numbers')
