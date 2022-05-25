# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 2 Take Home Problem 3 (20 points)
# e2-3_function.py: Write code for the two functions as specified by the comments below.

# 10 points
# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_letter
# Funtction parameters: none
# Returns: the validated user input
# Description:
# This function gets a letter from user input and verifies that the user
# entered a letter (a single character that is between letter A and Z, inclusive).
# The function keeps asking for user input until the user enters valid input.
# The letter entered by the user is returned as a capital letter.
def get_letter():
    doneLetter=False #flag variable
    letter=input('enter a letter: ')
    strang='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #figured out a better method than that whole if-or thing, using a string
    while not doneLetter:
        if letter.upper() in strang: # if the uppercase version of whatever entered is in the string
        #if letter.upper()=='A' or letter.upper()=='B' or letter.upper()=='C' or letter.upper()=='D' or letter.upper()=='E' or letter.upper()=='F' or letter.upper()=='G' or letter.upper()=='H' or letter.upper()=='I' or letter.upper()=='J' or letter.upper()=='K' or letter.upper()=='L' or letter.upper()=='M' or letter.upper()=='N' or letter.upper()=='O' or letter.upper()=='P' or letter.upper()=='Q' or letter.upper()=='R' or letter.upper()=='S' or letter.upper()=='T' or letter.upper()=='U' or letter.upper()=='V' or letter.upper()=='W' or letter.upper()=='X' or letter.upper()=='Y' or letter.upper()=='Z':#this is terrible, I know, I hope we aren't getting points off for style
            doneLetter=True
            return(letter.upper())
        else:
            print('incorrect input. try again') #if a correct input was not entered, it loops
            letter=input('enter a letter: ')



# end of get_letter function

# 10 points
# STUDENT MUST WRITE THIS FUNCTION
# Function name: find_letter
# Funtction parameters (type - desciption):
#    string - The string to search
#    string - The letter to search for
# Returns: nothing
# Description:
# This function looks for occurrences of the letter (second parameter) in the
# string (first parameter). If the letter is in the string, the function prints
# the position(s) where that letter occurs. If the letter is not in the string
# there is no output. The case of the string and the letter are ignored.

def find_letter(strung,letter):
    count=-1 #position is calculated through count
    for i in strung: #loops through the string
        count+=1
        if i==letter.upper() or i==letter.lower(): #case of the string and letter are ignored
            print(count)


# end of find_letter function

############################################################
# Do not alter the code below this line.
# You may comment out lines of code while you are testing your functions.
# Main part of program

print('Testing get_letter function:')
my_letter = get_letter()
print('You entered letter:', my_letter)
print()

print('Testing find_letter function:')
first = 'Hello World'
print('Looking for o in :', first)
find_letter(first, 'o')
print()

second = 'abcABCaBcAbc'
print('Looking for b in :', second)
find_letter(second,'b')
print()

print('Looking for z in :', second)
find_letter(second,'z')
