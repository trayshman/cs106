# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 2 Take Home Problem 2 (10 points)
# e2-2_dash.py: For each line of the file that contains a dash ('-'), replace the
# dash with a '&'. Print the line number and the revised text of that line. At
# the end of the program, print the total number of lines that were altered.
# If a line contains multiple dash characters, only replace the first one.
#
# Fix the errors this code.
# The two marked lines contain errors.
# Fix the errors by editing the two lines of code.
# You may not add or delete any lines of code.

fhand = open('quotes.txt')

x = 0

for line in fhand:
    line = line.strip()
    p = line.find('-')
    if p > 0: # FIX THIS LINE (4 points)
        x += 1
        print('\nOrignal:', line)
        rev = line[:p-1] + '&' + line[p+1:] #FIX THIS LINE (6 points)
        print('Altered:', rev)
print()
print(x, 'lines were altered')
