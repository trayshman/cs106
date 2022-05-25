# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 1 Take Home Problem 2 (15 points)
# e1-2_airline.py: Determines if a customer qualifies for premier frequent
# flyer status based on their lifetime miles, how many miles they have flown
# in the past year, how many flights they have taken in the past year, and
# fee paid.

# DO NOT MODIFY THIS BLOCK OF CODE
# Get input from the user. Assume the user enters valid input.
life_mi = int(input('What are your lifetime miles? '))
year_mi = int(input('How many miles have you flown this year? '))
year_flts = int(input('How many flights have you taken this year? '))
fee = int(input('What fee have you paid? $'))
print('----------')
# END OF BLOCK THAT SHOULD NOT BE MODIFIED

# CORRECT 5 ERRORS IN THE CONDITIONAL STATEMENTS AND/OR EXPRESSIONS BELOW
# The criteria for qualifying for the best rate are provided on the PDF file.
# You may only change the lines that are marked as needing corrections.
# Each marked line requires one or more corrections.

if year_mi >= 100000 or life_mi >= 500000: # Correct this line
    qualify = True
elif year_flts >= 40 and fee == 600: # Correct this line
    qualify = True
elif year_mi >= 30000 and fee == 300: # Correct this line
    qualify = True
else:
    qualify = False

# END OF BLOCK THAT SHOULD BE MODIFIED
# DO NOT MODIFY BELOW THIS LINE
if qualify:
    print('Congratulations, You are a premier frequent flyer!')
else:
    print('Sorry, you do not qualify')
