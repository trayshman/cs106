# extract_host.py
# Author: Christine F. Reilly
# Demonstration of using string slicing and string methods to extract part of a
# string that matches a certain pattern.

# Sample string
str = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# Extract the part of the email address that follows the @ character
# Assume there is one email address per string
# Assume that the @ character only appears as part of an email address

# Step 1: find the beginning of the part of the string to extract
# The first character to extract is the one immediately after the @ character
start = str.find('@') + 1

# Step 2: find the end of the part of the string to extract
# The last character to extract is immediately before the first space that
# follows the @ character. We can save the position of that space because
# the string split end number is one past the last character we want to get.
# Use the version of the find method that allows us to specify where to begin
# the search.
end = str.find(' ', start)

# Step 3: Use the string slicing functionality to extract the desired string
host = str[start:end]

print('Extracted string:', host)
