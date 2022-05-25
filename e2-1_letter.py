# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 2 Take Home Problem 1 (20 points)
# e2-1_letter.py: Asks the user to enter a letter and an integer.
# Counts the number of times this letter appears in each line of the file and
# how many lines have the specified number of this letter (the case of the
# letter is ignored).
# Prints (to the screen) the first line that had the specified number of this
# letter, and the number of lines that have the specified number of this letter.
#
# You may assume the user enters valid input. No error checking is necessary.
#
# Tasks to complete in this problem:
#   * (1 point) Get a letter from user input.
#   * (1 point) Get an integer from user input.
#   * (7 points) Count the number of times the specified letter appears in each
#     line of the input file. Ignore the case of the letter: both lowercase and
#     uppercase of the specified letter count the same.
#   * (5 points) Count the number of lines of the input file with the specified number of
#     occurrences of the specified letter.
#   * (5 points) Save the first line that has the specified number of occurrences of the
#     specified letter.
#   * (1 point) At the end of the program print:
#     - The number of lines that have the specified count of the specified letter.
#     - The first line with this count of the specified letter.

# Use quotes.txt as the example input file
fhand = open('quotes.txt')

# Write your code for this problem here:
letter = input('enter a letter: ')
num = int(input('enter a number: '))
thefirstline='' #intialize an empty string
linecount=0
goodlinecount=0
firstline=False
for line in fhand: #goes through each line in the file
    lettercount=0 #initializes letter count back to zero, important when we switch to the next line 
    linecount+=1 #counts lines
    for i in line: #goes through each character in the line
        if i==letter.lower() or i==letter.upper(): #if a character in the line is the letter entered, ignoring case
            lettercount+=1 #important for determining how many times it showed up in the line
    if lettercount==num: #because if it showed up the number of times as the number entered by the user
        goodlinecount+=1 #counts the number of lines that meet the requirements
        while firstline == False:
            thefirstline+=line #adds that line to the empty string
            firstline = True #flag variable turns true, to signify the first line meeting the requirements has been found

print(goodlinecount,'lines have the letter',letter,'printed',num,'times')
print('first line with',num,'of','letter: ')
print(thefirstline)
