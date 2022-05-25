# CS106 Lab
# October 14, 2021
# Names and roles of group members: Ryan Jones

######################################################################
# Problem 1 (Textbook exercise 8.2)
# Learning goal: Practice string methods, output formatting, and reading a file
# Spend up to 30 minutes working on this problem.
print('***** Problem 1:') # Do not change this line of code

# Write a program to read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.
#
# Your output must have exactly 4 digits to the right of the decimal point.
#
# Recall the examples from class on October 6:
#  * Output formatting
#  * Example where we extracted the floating point number from a string of this format.
#
# Recall that you calculated an average in Problem 2 from lab group work on September 23.
#
# Use the class examples and previous lab problem to help you solve this problem.
#
# Test your code on the input files: mbox-short.txt and mbox.txt
#

# First test your code using mbox-short.txt as the input file.
# Once your code works with the smaller file, test it with mbox.txt.
# Comment out the line that sets fname to the file you are not using.
#fname = 'mbox-short.txt'
fname = 'mbox.txt'

print('Input file:', fname)
f_read1 = open(fname)

# Write your code for Problem 1 here
count=0
sum=0
for a_line in f_read1:
    if a_line.startswith('X-DSPAM-Confidence:'):
        start = a_line.find('0')
        end = a_line.find(' ', start)
        num=a_line[start:end]
        num=float(num)
        count+=1
        sum+=num

print('Average spam confidence:%.4f' % (sum/count))


######################################################################
# Problem 2 (Similar to Textbook exercise 8.3)
# Learning goals: Practice file input and string methods.
# Spend up to 30 minutes working on this problem.
print('\n\n***** Problem 2:') # Do not change this line of code

# Write a program to read through the input file and look for lines that are
# between 40 and 50 characters (inclusive) and contain a colon ":".
# For each matching line output its line number in the file as well as the text.
# At the end, report the number of lines that were matched.
#
# Test your code on the input file: quotes.txt

f_read2 = open('quotes.txt')

# Write your code for Problem 2 here
count=0
linecount=0
for line in f_read2:
    if len(line)>=40 and len(line)<=50:
        if not line.find(':')==-1: #otherwise it would always return true, meaning it would count every line. this is "if not no colon"
        #if line.find(':') != -1 ALSO WORKS!!!
            linecount+=1
            print(linecount,line)
            count+=1

print('number of lines:',count)
