# letter_count.py
# This builds on the dict_demo.py example program from Part 3
# Author: Christine F. Reilly
# Counts the letters in a file
# Demonstration of: dictionary, string translate, tuples

import string # need the string module for the list of punctuation characters

# Read characters from a file. Use a dictionary to keep a count of each character.
char_count = dict() # Create an empty dictionary to keep track of letters

# Ask the user to enter the file name, then open the file
# For this demonstration we assume the user enters a valid file name and will
# not use a try-except-finally structure for file processing
fname = input('Enter the file name: ')
fhand = open(fname)

# Create the translation object for removing punctuation from a string
# Notice that the string module is imported at the top of this file
remove_chars = string.punctuation + ' ' # include space in the list of characters to be removed
no_punct = str.maketrans('', '', remove_chars)

# Iterate over the lines in the file
for line in fhand:

    # Strip leading and trailing whitespace from the line and convert all characters to lowercase
    good_line = line.strip().lower()

    # Remove punctuation and space characters from the line
    good_line = good_line.translate(no_punct)

    # Iterate over the characters in the line
    for c in good_line:

        if c not in char_count:
            # The character is not in the dictionary
            # add the character and initialize its count to 1
            char_count[c] = 1
        else:
            # The character is in the dictionary
            # add one to the count of this character
            char_count[c] += 1
    # End of loop through characters in the line
# End of loop through lines in the file
fhand.close()

# Print the dictionary and some information about it
print('The dictionary contains', len(char_count), 'items:')
print(char_count)

# Print one dictionary item per line
# Iterate over the items in the dictionary
print('\nA nicer printing of items in the dictionary:')
for key in char_count:
    # print in the format key : value
    print(key, ':', char_count[key])
# End of loop through the dictionary

print('\nThe dictionary items in lexicographic order:')

# Use the keys method to get the keys of the dictionary
# Use the list function to create a list of the keys
key_list = list(char_count.keys())

key_list.sort() # Sort the list of keys

# Iterate over the sorted list of keys
for k in key_list:
    # Print the key and its associated value from the dictionary
    print(k, char_count[k])

# Print the letters in order of the most common letter first
print('\nThe dictionary items in order of most common letter:')

# Create a list of tuples
# Each tuple is (value, key) from the dictionary
vk = [] # initialize the list

# Use the items method to get the key, value pairs from the dictionary
# Convert the items view to a list so we can iterate over it
for key, val in list(char_count.items()):
    # Add a tuple containing the value and the key to the list
    vk.append( (val, key))

# Sort the value-key list in reverse order. This will sort the list by value.
# If there are multiple items with the same value, they will then be sorted by key.
vk.sort(reverse=True)

# Print the sorted value-key list
for val, key in vk:
    print(val, key)
