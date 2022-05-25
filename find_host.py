# find_host.py
# Author: Christine F. Reilly
# Example of searching a file for lines that contain the email host 'uct.ac.za'
# Uses the string method: find
# Also demonstrates using try-except-finally with files

f_in = input('Enter the input file name: ')
f_read = None

f_out = input('Enter the output file name: ')
f_write = None

print('\nPrinting lines in the file that contain the email host "uct.ac.za:"\n')

# Place all file operations inside a try block
try:
    # Reading file step 1: Open the file
    f_read = open(f_in)

    # Open the output file
    f_write = open(f_out, 'w')

    # Reading file step 2: iterate over each line in the file
    for line in f_read:
        # Use the string strip method to remove leading and trailing whitespace from the string
        good_line = line.strip()

        # Step 3: For each line, do something with the data
        # Use the startswith string method to identify lines that begin with 'From:'
        if good_line.find('@uct.ac.za') != -1:
             # the write method does not automatically add a new line character
            f_write.write(good_line + '\n')
except Exception as err:
    # This except block of code will execute if there was an error in the try block.
    # By creating an Exception variable (err), we can print the specific error message.
    print('File cannot be processed, caused by:', err)

    # We encountered an error, end the program
    quit()
finally:
    # This finally block will always execute.
    print('In the finally block')
    # If there are no errors in the try block, the execution of the finally block
    # will follow the execution of the try block.
    # If an error resulted in the except block running, this finally block will
    # also run.
    # We use a finally block because it is important to close a file that we
    # opened. In programming, you clean up after yourself!
    if f_read != None:
        print('closing the input file')
        # Reading file step 4: close the file
        # We verify that fhand is assigned to a value to avoid an exception
        f_read.close()

    if f_write != None:
        print('closing the output file')
        # Reading file step 4: close the file
        # We verify that fhand is assigned to a value to avoid an exception
        f_write.close()
