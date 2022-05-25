# CS106 Lab
# November 11, 2021
# Names and roles of group members: Recorder: Ryan Jones Organizer: Yuqian Sun

######################################################################
# Problem 1 (Based on Textbook execise 10.3)
print('***** Problem 1:') # Do not change this line of code
# Learning goals: Practice using a dictionary structure, gain additional
# practice with strings and with reading from a file.
#
# The files mbox-short.txt and mbox.txt contain the series of email messages
# to process.
#
# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary. The steps for solving this problem are outlined below.
#

# Step 1 (code provided): Open the file.
#fname = 'mbox-short.txt'
#fname = 'mbox.txt'
#fname = 'mbox-rep.txt' # Use when testing Problem 3
fname = 'mbox-sing.txt' # Use when testing Problem 3
fhand = open(fname)

# Step 2: Create an empty dictionary object

prob1=dict()

# Step 3: Read the file. Use a dictionary to keep a count of how many email
# messages are sent by each sender.
# To identify the email addresses, look for lines in the file that begin with
# 'From:' The email address is the second word on these lines.
count=0
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        parts=line.split()
        #email=line[6:]
        email=parts[1]
        if email not in prob1:
            prob1[email]=1
            count+=1
        else:
            prob1[email]+=1



# Step 4: Close the input file
fhand.close()

# Step 5: Print the number of senders' addresses found in the file
print('the file contains',count,'senders email addresses')

# Step 6: Print the dictionary with one key-value pair per line

for key in prob1:
    print(key,':',prob1[key])

# Problem 2 (Based on Textbook exercise 10.4):
print('\n\n***** Problem 2:') # Do not change this line of code
# Learning goals: Practice using a dictionary structure, gain additional
# practice with finding maximum values.
#
# This problem uses the dictionary you created in Problem 1.
#
# Figure out who sent the most email messages. You may assume that there is
# exactly one sender with the maximum number of messages.
#
# Use a loop to look through the dictionary and find who has the most messages
# (see textbook Section 5.8.2 for an example of code that finds the maximum).
# Print the maximum number of messages the address of the sender that has this
# count of messages.
#
# Requirements for Problem 2:
# - Use the dictionary object you created in Problem 1.
# - Use a loop to find the maximum number of email messages, and the address of
#   the person who has that maximum number.
# - Print the maximum number of messages and the person who has that number
#   of messages.
maximum=None
maxEmail=None
for key in prob1:
    if maximum==None or maximum<prob1[key]:
        maximum=prob1[key]
        maxEmail=key
print('Maximum number of messages from a sender:',maximum)
print(maxEmail)


# Problem 3 - Bonus problem
# Work on this problem if you finish Problems 1 and 2.
# Learning goals: Practice using dictionary and list structures, gain additional
# practice with finding minimum values.
#
# Modify your code for Problem 2: find the minimum number of messages and keep
# a list of the persons who have this minimum.
# - Use a list to store the email address of the person(s) who have the
#   minimum number of messages.
# - Print the minimum number of messages and the person(s) who have that number
#   of messages.
#
# Two additional input files are provided to test Problem 3:
# - mbox-rep.txt: A modified version of mbox-short.txt where the minimum is not 1.
#   This file was created by reapeating some messages.
# - mbox-sing.txt: A modified version of mbox-short.txt where there is one
#   person who has the minimum number of messages.
#   This file was created by reapeating some messages.

minimum=None
minlist=[]
for key in prob1:
    if minimum==None or minimum>prob1[key]:
        minimum=prob1[key]
        minlist=[]
        minlist.append(key)
    elif minimum==prob1[key]:
        minlist.append(key)

print('Minimum number of messages from a sender:',minimum)
for c in minlist:
    print(c)
