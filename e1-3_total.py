# Your name: Ryan Jones

# CS106-1 Fall 2021
# Exam 1 Take Home Problem 3 (15 points)
# e1-3_total.py: Asks the user to enter a starting value for the current total.
# Subtracts from or adds to the current total based on the rules listed below,
# stopping when the current total is less than zero.
#
# Rules for adjusting the current total:
#  * If the user enters a number that is divisible by 10, subtract 10 from the total.
#  * If the user enters a number that is not divisible by 10 but is divisible
#       by 4, add 4 to the total.
#  * Otherwise subtract 5 from the total.
#
# Assume the user always enters valid input.
#
# Tasks to complete in this problem:
#   * (2 points) Get the starting value from the user.
#   * (5 points) Use a loop to keep asking for user input until the total
#        is less than 0.
#   * (6 points) Adjust the total based on the rules listed above.
#   * (2 ponts) Print the value of the total at the beginning of each loop iteration.
#
# Write your code for this problem here:
total=int(input('enter the starting value as an integer: '))


while total>=0:
    print('the current total is',total)
    integ=int(input('enter an integer: '))
    if integ%10==0:
        total-=10
    elif integ%4==0:
        total+=4
    else:
        total-=5

print('all done!')
