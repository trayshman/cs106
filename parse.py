


str= 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# Extract the part of the email address that follows the @ character
# Assume there is one email adress per string
# Assume that the @ character only appears as part of an email address

# We will use string slicing: need the start and the end point

# Step 1: find the starting point
# Use the find method to locate the index of the @ character
# The start point will be the index after the @ character

start = str.find('@') + 1
print(start)

# Step 2: find the end point
# The end point is after the start point
# The end point is the first space that follows the @ character
end = str.find(' ',start)
print(end)

# step 3: use string slicing to extract the part of the email address
host = str[start:end]

print(host)
