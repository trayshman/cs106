# class_size.py
# Author: Christine F. Reilly
# This program calculates the total number of people in the class

# Get user input for the number of students and professors
num_students = input('How many students are in the class? ')
num_prof = input('How many professors are in the class? ')

# Convert the strings entered by the user to integers
s = int(num_students)
p = int(num_prof)

# Calculate the total number of people in the class
total = s + p

# Print the result to the user

# Note: the following statement does not work because an int cannot be
# concatenated to a string
# print('There are ' + total + ' people in the class.')

# There are multiple ways to solve this problem.
# One way is to convert the int to a string
print('There are ' + str(total) + ' people in the class.')

# Another way is to separate items in the print function with a comma
print('There are', total, 'people in the class.')

# We will learn more options for formating output later this semester.
