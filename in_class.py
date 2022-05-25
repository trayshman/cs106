# Read characters from a file
# Use dictionary to keep count of the characters

# Create an empty dictionary
char_count = dict()

# Open a text file
fhand = open('q.txt')

# iterate over each line in the file
for line in fhand:

    # Strip leading and trailing whitespace
    line = line.strip()

    # Convert all letters to lowercase
    lower_line = line.lower()

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
