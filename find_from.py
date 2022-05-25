# find_from.py
# Author: Christine F. Reilly
# Example of searching a file for lines that begin with 'From:'
# Uses the string method: startswith

fname = input("Enter the file name: ")
fhand = None

print('\nPrinting lines in the file that start with "From:"\n')

# Reading file step 1: Open the file
# Put the call to the open function inside a try block.
# This will allow the exception to be caught if the file does not exist.
try:
    fhand = open(fname)

except Exception as err:
    # This except block of code will execute if there was an error in the try block.
    # By creating an Exception variable (err), we can print the specific error message.
    print('File', fname, 'cannot be processed, caused by:', err)
    print('Ending the program.')

    # We encountered an error, end the program
    quit()

# Reading file step 2: iterate over each line in the file
for line in fhand:
    # Use the string strip method to remove leading and trailing whitespace from the string
    good_line = line.strip()

    # Step 3: For each line, do something with the data
    # Use the startswith string method to identify lines that begin with 'From:'
    if good_line.startswith('From:'):
        print(good_line)
# End of loop through file

# Step 4: Close the file
fhand.close()
