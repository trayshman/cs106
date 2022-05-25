# Your Name: Ryan Jones
# CS106 Programming Assignment 8
# Data Processing

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
# STUDENT MUST WRITE THIS FUNCTION
# Function name: domain_type
# Function parameters (type - description):
#    list of lists - The database; this function does not modify this parameter
#    int - The index of the column to search
# Returns: A dictionary where the keys are top level domains and the values
#          are a count of how many times that top level domain was found.
# Description:
# This function reads the data in a specific column of a database. It is assumed
# this column contains email addresses. The top level domain is extracted from
# the email address using the pattern that the whole domain is to the right of the @
# character and the top level domain is the part of the domain to the right of the
# first period character. A dictionary is used to count the number of times
# each top level domain occurs in the database, and the function returns this
# dictionary.

def domain_type(data,num):
    a=dict() #create dictionary
    for j in data: #for each row in the data
        email=(j[num]) #assumes collumn contains email address, assigns it to email variable
        at=email.find('@') #finds the @ in the email
        domain=email[at+1:] #the domain is the part of the email after the @
        dot=domain.find('.') #finds the dot in the domain
        topdom=domain[dot+1:] #the top domain is the part of the domain after the dot
        if topdom not in a:
            # The dictionary does not have an entry for this character
            # Add character to dictionary, initialize its count to 1
            a[topdom] = 1
        else:
            # The character has been seen before, is already in dictionary
            # Add one to the count for this character
            a[topdom] += 1
    return(a)

# end of domain_type function


############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: print_d_sort
# Function parameters (type - description):
#    dictionary - The dictionary to print; this function does not modify this parameter
# Returns: nothing (void function)
# Description: This function prints the each key and associated value from a
# dictionary with one key-value pair per line, and the output with keys in
# sorted order.

def print_d_sort(dict):
    key_list = list(dict.keys()) #makes a list of the keys

    # sort the list of key_list
    key_list.sort()

    for k in key_list:
        print(k,':',dict[k]) #prints one key-value pair per line, and it's all sorted


# end of print_d_sort function


############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: col_dictionary
# Function parameters (type - description):
#    list of lists - The database; this function does not modify this parameter
#    int - The index of the column for the key data
# Returns: a dictionary where the key is the data from the column specified by
#    the second parameter and the value is the database row. The number of entries
#     in the dictionary is the same as the number of rows in the list of lists parameter.
# Description: This function creates a dictionary that has one entry per row
# in the list of lists parameter. The dictionary key is the value from the column index
# specified by the second paramter and the dictionary value is the entire row.

def col_dictionary(data,num):
    a = dict() #create dictionary
    for line in data: #for each line in the data
        key = line[num] #assigns the specified column to the variable key
        a[key]=line #a dictionairy where the key is the data from the column
    return(a) #returns it


# End of col_dictionary function


############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: lookup
# Function paramters (type - description):
#     dictionary - The data to search.
#     string - The prompt for user input.
# Returns: nothing
# Description: This function prompts the user for input using the second
# parameter. As long as the user does not enter 'done', this function uses the
# input as the key for the dictionary and prints the value associated with that
# key. If there is no dictionary entry for the key entered by the user, the function
# prints a message stating that no entry was found.
# Tip: If there is not a dictionary entry for a key, Python throws an exception.
# You can use a try-except structure to gracefully handle this exception.

def lookup(dict,strung):
    prompt=input(strung) #gets the user input
    while prompt != 'done': #while the user input isnt 'done'

        try:
            val=dict[prompt] #uses the input as the key for the dictionary and prints the value associated with that key
            print('found:',val)
            prompt=input(strung) #and then prompts the user again


        except: # if there was no entry for the key found, an exception in the above code will prompt this
            print('no entry found') #lets the user know
            prompt=input(strung) #re-prompts the user

# End of lookup function


# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
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
# Function for test 2: dictionary of domain counts
def test2(db2):
    print('\n\n********** Test 2 **********')

    # Create a dictionary with each email domain and its count
    domain_counts = domain_type(db2, 3)

    # Print the dictionary sorted by the email domain
    print_d_sort(domain_counts)

############################################################
# Function for test 3: lookup based on value in a database column
def test3(db3):
    print('\n\n********** Test 3 **********')

    # Create a dictionary of each phone number and its row
    d = col_dictionary(db3, 4)

    # Call the lookup function to ask the user to enter a phone number
    # then lookup the row that contains that phone number
    lookup(d, 'Enter a phone number to find a database entry: ')


############################################################
# Main part of program

# Call the function to load the customer data into a list
cust_db = load_customer('cust.txt')

# Run the tests for this assignment
test1(cust_db)

test2(cust_db)

test3(cust_db)
