# place_in_line.py
# Author: Christine F. Reilly
# Recursive way to determine your place in line

# Function name: line_pos
# Function parameter: none
# Returns: The "person's" positition in the line
# Description:
# This function uses recursion to determine the hypothetical person's place
# in a hypothetical line.
def line_pos():
    # Get user input to determine if the current person is at the front of the line.
    # Assume the user enters valid input.
    front = input('Is there a person in front of you? (enter y/n) ')
    if(front == 'n'):
        # Base case: you are at the front of the line
        print('in line_pos function: front of the line')
        return 1
    else:
        # Recursive case: you are not at the front of the line.
        # Make a recursive call to this function to simulate asking the person
        # in front of you.
        ahead_pos = line_pos()
        print('in line_pos function: ahead_pos =', ahead_pos)
        # Your position is the position of the person ahead of you, plus yourself
        return ahead_pos + 1
# End of line_pos function

# Main part of program
print('What is my position in this line?')
my_pos = line_pos()
print('I am at position', my_pos)
