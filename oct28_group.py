# CS106 Lab
# October 28, 2021
# Names and roles of group members: Recorder: Ryan Jones Organizer: Yuqian Sun

######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code
# Learning goals: Practice working with a list, and get more experience reading
# data from files.
#
# Using the same input file as we used for Programming Assignment 5, this program
# demonstrates that in some cases it is useful to read data from an input file
# and store it in an array. When the data from the file must be examined many
# times, storing the data in an array saves the work of reading the input file
# many times.
#
# In this problem, you will count the number of times a particular value was the
# daily average temperature at Albany in 2020. The user can choose to repeat
# this action.
#
# Write code for the steps as indicated by the comments below.

# Step 1 (code provided): Open the data file
# Notice that this is the same data file as we used for Programming Assignment 5.
fhand = open('alb_weather_2020.txt')

# Step 2 (write this code): Create an empty list
a = []

# Step 3 (write this code):
# Read each line of the file.
# Only process lines that begin with 'GHCND'.
# Use the split method to break the line into tokens.
# Save the daily average temperature (as an int type) into the array you created
#   in Step 2. The daily average temperature is at index 10 of the list returned
#   by the split method.

for line in fhand:
    good_line=line.strip()
    if good_line.startswith('GHCND'): #ignore the headers of the text file
        parts=good_line.split() #tokenize
        tempAv = parts[10]
        tempAv = int(tempAv)
        a.append(tempAv)


# Step 4 (write this code): Close the input file.
fhand.close()

# Step 5 (write this code):
# Using a loop, keep repeating this step as long as the user wishes to continue.
# Ask the user to enter a temperature.
# Count the number of times that value appears in the list of daily average
#    temperatures.
# Print a message telling the user how many times their value appeared in the list.
# You may assume the user always enters valid input.
done = False

while not done:
    count = 0
    temp = int(input('What temperature do you want to count?: '))
    for w in a:
        if w==temp:
            count+=1
    print(temp,'is found',count,'times in the temperature list')
    inquire = input('would you like to continue? [y/n]: ')
    if inquire == 'y':
        done = False
    if inquire == 'n':
        done = True




######################################################################
# Problem 2 -- Bonus Problem (Exercise 9.4 from the textbook)
print('\n\n***** Problem 2:') # Do not change this line of code
# Learning goals: Practice working with a list, get more experience working with
# strings, and get more experience reading data from files.
#
# Write code to open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is
# not in the list, add it to the list. After reading the file sort and print the
# resulting words in alphabetical order. (Note: this ordering is technically
# called lexicographic order because it is based on the character symbols.
# Notice that words that start with a capital letter are placed before words
# that start with a lowercase letter.)
#
# Helpful tips:
#
# There is a sort method that will sort the contents of a list.
# For example, if you have a list called a_list, the following code will
# sort the values in the list:
#     a_list.sort()
#
# The in operator will evaluate to true if a list contains an item. For example, if
# you have a list called a_list, the following code will evalutate to true if
# a_list contains the value 106:
#     106 in a_list
# The not in operator will evaluate to true if a list does not contain an item.
# For example, the following code will evaluate to true if a_list does not
# contain the value 106:
#     106 not in a_list
#
# Write your code for Problem 2:
fhand = open('romeo.txt')
list = []

for line in fhand:
    words = line.split()
    for i in words:
        if i not in list:
            list.append(i)

list.sort()
print(list)
