# CS106 Lab
# December 2, 2021
# Names and roles of group members: Ryan Jones, Yuqian Sun

import re

######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code
# This problem is based on Exercise 12.2 from the textbook.
#
# Learning goal: Practice using regular expressions to find lines in a file that
# match a pattern and extract data from these matching lines.
#
# Write a program to read lines of text from a file and look for lines of the
# form
#    New Revision: 39772
# Use a regular expression and the findall() method to find matching lines and
# extract the number from each matching line. Compute the average of the numbers
# and print out the average.
#
# The pattern to match is:
# * line contains two words, a colon, then an integer, and nothing else.
#
# Requirements:
# * You must use regular expressions for finding lines that match the given pattern
#   and for extracting the number from matching lines.
# * The regular expression should match any line with the same pattern. It should
#   not match only the specific text shown in this example.
# * The only string method you may use is strip().
#
# Tips for working on this problem:
# * First write and test the regular expression.
#     - Work on the regular expression one part at a time. For example: first print
#       all lines that start with two words followed by a colon. Then add the
#       requirement that an integer follows the colon and is at the end of the line.
# * Once you know your regular expression works, write the code to extract the
#   integer from the matching lines and find the average of these integers.

fname = 'mbox-short.txt'
#fname = 'mbox.txt'
fhand = open(fname)

# Write your code for Problem 1
count=0
total=0
for line in fhand:
    line = line.strip()

    #if re.search('[a-zA-Z0-9]\s+[a-zA-Z0-9]:[0-9]$', line):
    if re.search('^[a-zA-Z0-9]+\s+[a-zA-Z0-9]+:\s+[0-9]+$', line):
        numbers = re.findall('[0-9]+', line)
        for n in numbers:
            num=int(n)
            total+=num
            count+=1

print('average:',total/count)







######################################################################
# Problem 2 (Bonus Problem)
print('\n\n***** Problem 2 (Bonus Problem):') # Do not change this line of code
# Learning goals: More practice with regular expressions
#
# Use a regular expression and the findall method to extract the upper level
# domain from lines that specify the sender of an email.
#
# Start with the regular expression we used in the email_lines function example
# from class. This regular expression matches the lines in an email
# header that specifies the sender of an email (lines of the form 'From: user@domain.upper').
#
# Modify this regular expression and use it to extract the upper level domain
# from the email address. Define the upper level domain as the text that follows
# the first period after the @ character. See the sample output for examples.
#
# After you have created the regular expression, write similar code as you did
# in Programming Assignment 8 to create a dictionary where the key is the top
# level domain and the value is the count of the number of lines that match that domain.
#
# Print the dictionary items in a format similar to that shown on the sample output.
#
# Requirements:
# * You must use regular expressions for finding lines that match the given pattern
#   and for extracting the upper domain from matching lines.
# * The only string method you may use is strip().
# * Use a dictionary structure to count the number of occurrences of each upper domain.
#
# Tips for working on this problem:
# * Only a few modifications need to be made to the regular expression from
#   class. The changes mostly use techniques discussed in class on December 1.
# * Use the same approach as Problem 1: first test your regular expression. Once
#   you have a correct regular expression, write the rest of the program.
#
# Write your code for Problem 2:

# This is the regular expression from the email_lines function from class.
# Modify this regular expression to meet the requirements of this problem.
#email_regex = '^From:\s*[a-zA-Z0-9]\S*@\S*[a-zA-Z]$'

# fname = 'mbox-short.txt'
fname = 'mbox.txt'
fhand = open(fname)

# Write your code for Problem 2
