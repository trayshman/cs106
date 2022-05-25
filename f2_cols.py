# Your name: Ryan Jones

# CS106 Fall 2021
# Final Exam Take Home Problem 2 (10 points)
# f2_cols.py: Correct the errors in the code.

# INSTRUCTIONS: Correct the logic and/or semantic errors in two functions:
# read_table and sum_col.
# After the code is corrected the output from this program should match the sample output.
#
# Follow the rules for corrections provided with each task.
# Recommended approach: Make a copy of the section of code, comment out the
# original and make your changes to the copy. This allows you to easily see the
# original function while you work on this problem.
# Tip: The errors are related to the concepts of lists.

############################################################
# TASK 1 (5 points)
# STUDENT MUST FIX THE ERRORS IN THIS FUNCTION
# Function name: read_table
# Function parameter:
#    string - The name of the file
# Returns: A list of lists (two-dimensional list or table)
# Description:
# This function reads integers from a file into a table (a list of lists).
# Each line of the file is stored as one row in the table. The numbers in the
# file are seprated by a comma.
#
# Rules for corrections in Task 1:
#   * Add two lines of code.
#   * Modify one line of code.
#   * Only alter the code between the comments that indcate the beginning and
#     end of the block that contains errors.
def read_table(fname):
    fhand = open(fname)

    table = []
    for line in fhand:
        line = line.strip()
        nums = line.split(',')

        # Beginning of block of code that contains errors
        row=[]
        for n in nums:
            row.append(n)
        table.append(row)

        # End of block of code that contains errors

    return table
# end of read_table function


############################################################
# TASK 2 (5 points)
# STUDENT MUST FIX THE ERRORS IN THIS FUNCTION
# Function name: sum_col
# Function parameter:
#    list of lists containing integers
# Returns: A list containing the sum of each column in the parameter table.
# Description:
# This function iterates over a table (a list of lists). It finds
# the sum of the integers in each column and saves that sum into another list.
#
# Rules for corrections in Task 2:
#   * You may only modify the lines marked with the "fix this line" comment.
#   * You may not add or delete lines of code.

# Return a list where each item is the sum of the corresponding column from the
# list of lists
def sum_col(t):
    colsum = [] #initialize empty list where each item will be the sum of the corresponding column from the list of lists (the table)

    for x in t[0]: # for each number in the first row
        colsum.append(int(x)) # fix this line    the number is appended to colsum

    for row in t: # for each row in the table
        for col in range(len(row)): # fix this line
            colsum[int(col)] += int(row[col]) # fix this line

    return colsum
# end of sum_col function


# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have corrected the functions above, your functions must work with the
# code that is provided below.

# print the list of lists as a table
def print_table(t):
    for row in t:
        for col in row:
            print(col, end=' ')
        print()
# end of print_table function


# main part of program
my_table = read_table('values.txt')

# If the read_table function is not completed, uncomment the line of code
# below and use this list of lists to test the other function.
# my_table = [[123,456,789],[111,222,333],[444,555,666],[777,888,999],[321,234,101]]

print_table(my_table)

cs = sum_col(my_table)
print('\nsum of each column:', cs)
