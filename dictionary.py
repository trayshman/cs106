# Read characters from a file
# Use dictionary to keep count of the characters

# Create an empty dictionary
char_count = dict()

# Open a text file
fhand = open('q.txt')

import string
#remove all punctuation and spaces from becoming keys
remove_chars = string.punctuation + ' ' #characters to not count
no_punct = str.maketrans('','',remove_chars) # create translation object



# iterate over each line in the file
for line in fhand:

    # Strip leading and trailing whitespace
    line = line.strip()

    # Convert all letters to lowercase
    lower_line = line.lower()
    lower_line = lower_line.translate(no_punct) # TRANSLATE THINGY
    # iterate over each character in the line
    for c in lower_line:
        if c not in char_count:
            # The dictionary does not have an entry for this character
            # Add character to dictionary, initialize its count to 1
            char_count[c] = 1
        else:
            # The character has been seen before, is already in dictionary
            # Add one to the count for this character
            char_count[c] += 1
    # end of loop of characters in a line
# end of loop of each line in the file

print('The dictionary contains', len(char_count), 'items')
print(char_count)

# print one dictionary item per line (one key-value pair per line)
print('\nPrinting one key-value pair per line')
for key in char_count:
    print(key,':',char_count[key])

print('\nPrinting sorted dictionary')
# print one dictionary item per line in lexicon order
key_list = list(char_count.keys())

# sort the list of key_list
key_list.sort()

for k in key_list:
    print(k,':',char_count[k])
