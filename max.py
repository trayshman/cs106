# max.py
# Author: Christine F. Reilly
# Find the largest value in a sequence, do not use the None value

# Declare a variable for the list of numbers
numbers = [3, 41, 12, 9, 74, 15]

# Assuming that the list could contain any values, a good choice is to
# initialize largest to the first item in the list.
# With list data, we use the square brackets and a position number to get
# a value out of the list (more about this in a few weeks)
largest = numbers[0]

# Loop through the values in the list
for num in numbers:
    # Compare the current value to the largest found so far
    if num > largest:
        # Found a new largest
        largest = num

# after loop
print('Largest:', largest)
