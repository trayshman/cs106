# email_dir_exercise.py
# Author: Christine F. Reilly
# Uses a dictionary to create a directory of names and email addresses.
# Demonstrates using a tuple as a dictionary key
# Contains solution for tuples exercise

# Create a dictionary to store the directory
dir = dict()

# Open the input file
fhand = open('emails.txt')

# Iterate over the lines in the file
for line in fhand:
    # Strip leading and trailing whitespace from the line, then split into
    # pieces using space as the delimiter
    pieces = line.strip().split()

    # Each line of the file contains: first_name last_name email
    # Save last_name, first_name into a tuple
    # Use this tuple as the dictionary key, and the email as the value
    k = (pieces[1], pieces[0])
    v = pieces[2]
    dir[k] = v
# end of loop through file

# Print the dictionary, sorted by last name
key_list = list(dir.keys())
key_list.sort()

for last, first in key_list:
    print(last + ', ' + first + ': ' + dir[last, first])

# Given a first and last name, print the email address
print('\nLookup an email address')
first = input('Enter first name: ')
last = input('Enter last name: ')

email = dir[last, first] # Finish this line of code

print('Email:', email)
