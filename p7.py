# Your Name:
# CS106 Programming Assignment 7
# Simple Database

# Simplifying assumptions:
# all fields are string type
# database contains a single type of data

############################################################
# STUDENT MUST WRITE THIS FUNCTION
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
    a=[]
    f_read=open(fname)
    for line in f_read:
        good_line=line.strip()
        parts=good_line.split('|')
        a.append(parts)

    return a


# end of load_customer function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
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
            print(t[i][j], end=' ** ')
        # After the inner loop, print an end of line
        print()


# end of print_db function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: select
# Function parameters (type - description):
#    list of lists - The database table; this function does not modify this parameter
#    string - The value to search for
#    int - The index of the column to search
# Returns: A list of rows that contain the specified columns.
# Description:
# This function returns a list of rows (a new database table) that exactly
# contains the specified value in the specified column. If no rows match the
# specified value, this function returns an empty list. This function assumes
# the colunm number parameter is an integer that is a valid column number
# (the function does not validate this parameter).

def select(desc,name,collumn):
    good=[]
    for i in desc:
        if i[collumn] == name:
            good.append(i)

    return good


# end of select function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: project
# Function parameters (type - description):
#    list of lists - The database table; this function does not modify this parameter
#    list - A list of integer indexes of the columns to include
# Returns: A list of lists
# Description:
# This function creates a new list of lists (a new database table) that has the
# same number of rows as the database parameter, and only includes the columns
# from the original table that are listed in the parameter that specifies the
# columns to include. This function assumes that the parameter containing the
# column numbers is a list of integers that are valid column numbers (the function
# does not validate this parameter).
#
# The function name is pronounced pruh-jekt (using the word as a verb, like
# projecting a video on a screen).

def project(a,collumn):
    goodlist=[] #is a list of lists

    for row in a:
        goodrow=[]
        for i in collumn:
            goodrow.append(a[i])
        goodlist.append(goodrow)


    return goodrow



# end of project function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: select_like
# Function parameters (type - description):
#    list of lists - The database; this function does not modify this parameter
#    string - The value to search for
#    int - The index of the column to search
# Returns: A list of rows that where part of the data in the specified column
#          matches the parameter string.
# Description:
# This function returns a list of rows (a new database table) where part of the
# data in the specified column matches the parameter string. This function assumes
# the colunm number parameter is an integer that is a valid column number
# (the function does not validate this parameter).

def select_like(desc,strung,collumn):
    good=[]
    for i in desc:
        if strung in i[collumn]:
            good.append(i)

    return good


# end of select_like function

# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# You may write additional test code.
# When you have completed the functions above, your functions must work with the
# code that is provided below.

############################################################
# Function for test 1: check database table size
# Verify that output from this test matches the example output posted on theSpring.
def test1(db1):
    print('\n\n********** Test 1 **********')

    print('number of rows:', len(db1))
    print('number of columns in first row:', len(db1[0]))
    print('number of columns in last row:', len(db1[len(db1)-1]))

############################################################
# Function for test 2: selection
# Verify that output from this test matches the example output posted on theSpring.
def test2(db2):
    print('\n\n********** Test 2 **********')
    result2 = select(db2, 'Wendy', 0)
    print('Result of Test 2-A:')
    print_db(result2)

    result2 = select(db2, 'Amelia', 0)
    print('\nResult of Test 2-B:')
    print_db(result2)

    result2 = select(db2, '(499) 558-4193', 4)
    print('\nResult of Test 2-C:')
    print_db(result2)

    result2 = select(db2, '(000) 000-0000', 4)
    print('\nResult of Test 2-D:')
    print_db(result2)

############################################################
# Function for test 3: selection and projection
# Verify that output from this test matches the example output posted on theSpring.
def test3(db3):
    print('\n\n********** Test 3 **********')
    result3 = select(db3, 'Wendy', 0)
    result3 = project(result3, [1,2])
    print('Result of Test 3-A:')
    print_db(result3)

    result3 = select(db3, 'Amelia', 0)
    result3 = project(result3, [3])
    print('\nResult of Test 3-B:')
    print_db(result3)

############################################################
# Function for test 4: select like
# Verify that output from this test matches the example output posted on theSpring.
def test4(db4):
    print('\n\n********** Test 4 **********')

    # Find email addresses that contain .org
    result4 = select_like(db4, '.net', 3)
    print('Result of Test 4-A:')
    print_db(result4)

    # Find last names that contain the letter k
    result4 = select_like(db4, 'k', 1)
    print('\nResult of Test 4-B:')
    print_db(result4)

    # Find last names that contain the letter k,
    # then project the First and Last name columns
    result4 = select_like(db4, 'k', 1)
    result4 = project(result4, [0,1])
    print('\nResult of Test 4-C:')
    print_db(result4)

    # Test when no rows match the pattern
    result4 = select_like(db4, 'xyz', 0)
    print('\nResult of Test 4-D:')
    print_db(result4)

############################################################
# Main part of program

# Call the function to load the customer data into a list
cust_db = load_customer('cust.txt')
test1(cust_db)

 #Uncomment the code below to print the entire database. This may be useful
# when you are testing your code.
#print('\nThe whole database:')
print_db(cust_db)

# Run the tests
# Verify that program output matches the example output posted on theSpring.
test2(cust_db)
test3(cust_db)
test4(cust_db)

print('\nFinished Tests')
