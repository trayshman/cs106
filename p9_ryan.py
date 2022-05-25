# Your Name: Ryan Jones
# CS106 Programming Assignment 9
# Recursion and Tuples

# Simplifying assumptions:
# all fields are string type
# database contains a single type of data

import random # Used in test3 function

# Use the seed to get test3 output that matches the sample output.
# Also run the program a few times without setting a seed and observe
# how the test3 output has slight variations.
random.seed(106)

############################################################
# USE YOUR FUNCTION FROM PROGRAMMING ASSIGNMENT 7
# Function name: load_customer
# Function parameter (type - description):
#    string - name of the input file
# Returns: list that contains the data for this database
# Description:
# This function reads data from file into a a list of lists that mimics a database.
# Each element of the outer list contains a list (inner list) with the data
# from one row of the file.
# The file uses the pipe character ('|') as the delimiter between fields.
# All data in the file is string type.

def load_customer(fname):
    a=[] #empty list
    f_read=open(fname) # open the file
    for line in f_read: #for each line in the file
        good_line=line.strip() #strip of all whitespace
        parts=good_line.split('|') #and split based on when | shows up in the line
        a.append(parts) # and add all those split parts to the empty list

    return a #and return it
# end of load_customer function


############################################################
# USE YOUR FUNCTION FROM PROGRAMMING ASSIGNMENT 7
# Function name: print_db
# Function parameter (type - description):
#    list of lists - The database table to print; this function does not modify this parameter
# Returns: nothing (void function)
# Description:
# This function prints a database table to the screen, with one row per line.
# Two astrisk characters (**) are printed between each field within a row.
# The last field in a row does not have astrisk characters printed after its data.
def print_db(t):
    for i in range(len(t)):
        # Inner loop: iterate over each column in the row
        for j in range(len(t[i])):
            print(t[i][j], end=' ** ') # print ** between each field within a row
        # After the inner loop, print an end of line
        print()

# end of print_db function


############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: select_row_lin
# Function parameters:
#    list of lists - The database table; this function does not modify this parameter
#    string - The value to search for
#    int - The index of the column to search
# Returns: A tuple where the first item is the row (a list) that contains the
# specified value in the specified column, and the second item is the number of
# rows that were examined by this method. If no matching row was found, the first
# item in the returned tuple is an empty list.
# Description:
# This function uses linear search to find the row in the database that exactly
# contains the specified value in the specified column.
# This function assumes that at most one row will match.
#
# Note - This function is similar to, but not the same as, the select function
# from Programming Assignment 7.

def select_row_lin(list,strung,num): #define function with database table, the value to search for, and index of column to search
    rownum=0 #initialize the count to 0
    for i in list: #for row in list
        rownum+=1 #counts each row
        if i[num] == strung: #if matching row found
            return (i,rownum) #returns the row and row number

    return ([],rownum) #no matching row found, returns empty list and rownum

# end of select_row_lin function


############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: sort_table
# Function parameters:
#    list of lists - The database table; this function does not modify this parameter
#    int - The index of the column to sort by
# Returns: A new list of lists where the rows are sorted by the specified column.
# Description:
# This function sorts the rows of the table by the specified column.
#
# Use the Decorate, Sort, Undecorate (DSU) pattern as demonstrated in Section
#   11.2 of the textbook to sort the table.
# Suggested steps for writing this function:
#    Step 1 (Decorate): create a list of tuples. The first item in the tuple is
#        the data to sort by; the second item in the tuple is the row of the table.
#    Step 2 (Sort): Use the sort method to sort the list of tuples.
#    Step 3 (Undecorate): Create the result list. This result will be the rows of
#        the table in order of the values in the column that was specified by the parameter.

def sort_table(lost,column): #define a function with the database table, and the index of the column to sort by
    t = list() #initialize a list of tuples
    for word in lost: # for row in database
        t.append((word[column], word)) #tuple added to list: data to sort by, row

    t.sort() #sort method
    res = list() #new list initialized for the tuples

    for column, word in t:
        res.append(word) #appended to that new list (undecorate)

    return res #returned new list

# end of sort_table function


############################################################
# STUDENT MUST MODIFY THIS FUNCTION
# Function name: select_row_bin
# Function parameters:
#    list of lists - The database table; this function does not modify this parameter
#    string - The value to search for
#    int - The index of the column to search
#    int - the starting row number of the subtable to search2
#    int - the ending row number of the subtable to search
# Returns: A tuple where the first item is the row (a list) that contains the
# specified value in the specified column, and the second item is the number of
# rows that were examined by this method. If no matching row was found, the first
# item in the returned tuple is an empty list.
# Description:
# This function uses binary search to find the row in the database that exactly
# contains the specified value in the specified column.
# This function assumes that at most one row will match.
#
# The code provided below is the binary_search function we discussed in class,
# modified to search the database table. An additional parameter, the index of
# the column to search, is added to the function header and the column index
# has been added in the parts of the code that compare the key with the middle value.
#
# YOUR TASK:
# Fix the two lines as indicated in the code for this function. This function
# returns a tuple where the first item is the row (a list) that contains the
# specified value in the specified column, and the second item is the number of
# database rows that were examined by this method.
#
def select_row_bin(db, key, index, startpos, endpos):

    # Calculate the middle position in the sublist. Use integer division
    # because list index must be an integer
    middle = (startpos + endpos) // 2

    # Uncomment these print statments if needed for testing and debugging
    # Print some information for tracing the recursive function calls
    #print('binary_search: key is', key, '; startpos is', startpos, '; endpos is', endpos)
    #print('middle is', middle, '; value at middle is', db[middle], '\n')

    if key == db[middle][index]:
        # Base case 1: found the key. Return the row that contains the key.
        return (db[middle], 1)
    elif key < db[middle][index]:
        # Key comes earlier in the list
        # Change the end position so that only the earlier part of the list
        # will be searched when this function is recursively called
        endpos = middle - 1
    else:
        # Key comes later in the list
        # Change the start position so that only the later part of the list
        # will be searched when this function is recursively called
        startpos = middle + 1

    # See if there are more words left to check
    if startpos <= endpos:
        # There are more words to check, recursively call this function
        answer = select_row_bin(db, key, index, startpos, endpos)

        return (answer[0],answer[1]+1) # Fix this line, it must return a tuple
    else:
        # Base case 2: No more words to check. The word is not in the list.
        return ([],1) #base case for not found: returns empty list and 1
# end of select_row_bin function


############################################################
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have completed the functions above, your functions must work with the
# code that is provided below.

############################################################
# DO NOT MODIFY THIS FUNCTION
# Function for test 1: select_row_lin
def test1(db):
    print('********** Test 1 **********')
    print('Testing select_row_lin:')

    sel = select_row_lin(db, 'French', 1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_lin(db, 'Larson', 1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_lin(db, 'Kim', 1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_lin(db, 'Gallagher', 1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_lin(db, 'Xyz', 1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])
# end of test1 function

############################################################
# DO NOT MODIFY THIS FUNCTION
# Function for test 2: select_row_bin
# Assumes that the database is sorted
def test2(db):
    print('\n********** Test 2 **********')
    print('Testing select_row_bin:')

    sel = select_row_bin(db, 'French', 1, 0, len(sort_db)-1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_bin(db, 'Larson', 1, 0, len(sort_db)-1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_bin(db, 'Kim', 1, 0, len(sort_db)-1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_bin(db, 'Gallagher', 1, 0, len(sort_db)-1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])

    sel = select_row_bin(db, 'Xyz', 1, 0, len(sort_db)-1)
    print('\nFound row:', sel[0])
    print('Number of comparisions:', sel[1])
# end of test2 function

############################################################
# DO NOT MODIFY THIS FUNCTION
# Function for test 3: compare_select
# First parameter: the original database
# Second parameter: the sorted database
def test3(db, sorted_db):

    print('\n********** Test 3 **********')

    # Extract a list of the last names from the original database
    last = []
    for row in db:
        last.append(row[1])

    # Run many rounds of the experiment
    # In each round, select a last name at random and call both of the select
    # functions.
    # Add the number of comparisions returned by each sort function to a
    # running total.
    rounds = 50
    lin_total = 0
    bin_total = 0
    for i in range(rounds):
        # Choose a random last name from the list
        name = random.choice(last)

        # Call the linear select function
        lin_sel = select_row_lin(db, name, 1)
        lin_total += lin_sel[1]

        # Call the binary select function
        bin_sel = select_row_bin(sorted_db, name, 1, 0, len(sorted_db)-1)
        bin_total += bin_sel[1]
    # end of rounds of the experiment

    # Calculate and print the statistics
    lin_avg = lin_total / rounds
    bin_avg = bin_total / rounds

    print('Ran', rounds, 'rounds of the select functions')
    print('select_row_lin examined', lin_avg, 'rows on average')
    print('select_row_bin examined', bin_avg, 'rows on average')


# Main part of the program

# Call the function to load the customer data into a list
cust_db = load_customer('cust_v2.txt')

# Convert the database from a list of lists to a tuple of lists.
# This ensures that functions cannot modify the database.
cust_db_tup = tuple(cust_db)

# Uncomment these print statments if needed for testing and debugging
#print('The whole database:')
#print_db(cust_db_tup)

test1(cust_db_tup)


# Sort the database based on last name
sort_db = sort_table(cust_db_tup, 1)

# Uncomment these print statments if needed for testing and debugging
#print('\n\nThe database sorted by last name:')
#print_db(sort_db)

test2(sort_db)

test3(cust_db_tup, sort_db)
