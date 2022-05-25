# Your Name: Ryan
# CS106 Programming Assignment 6
# Let's Make a Deal!

import random
# Use a seed for testing
# Comment this line out for different game play every time the program is run
#random.seed(106)

# STUDENT MUST WRITE THIS FUNCTION
# You may copy the code from October 21 lab
# Function name: get_int
# Funtction parameters:
#    integer - lower bound
#    string - input prompt
# Returns: the validated user input
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, and is greater than
# the lower bound.

def get_int(lower,prompt): #define function
    x=lower #set x to an unacceptable value
    while x<=lower: #while x is unacceptable (equal to or lower than lower)
        x=input(prompt) #input prompt
        try:
            x=int(x) #must be an integer
        except:
            print('you must enter an integer')
    return(x) #returns value

# end of get_int function


# STUDENT MUST WRITE THIS FUNCTION
# You may copy the code from October 21 lab
# Function name: get_int_range
# Funtction parameters:
#    integer - lower bound
#    integer - upper bound
#    string - input prompt
# Returns: the validated user input
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input is an integer, is greater than
# the lower bound, and is less than the upper bound.
def get_int_range(lower,upper,prompt): #define function
    x = lower # unacceptable value
    while x<=lower or x>=upper: #while value is below or equal to lower or greater than or equal to upper
        x=input(prompt) #prompt to change value
        try:
            x=int(x) #must be integer
        except:
            print('you must enter an integer')
    return(x) #returns value

# end of get_int_range function


# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_choice
# Funtction parameters:
#    string - first valid choice
#    string - second valid choice
#    string - input prompt
# Returns: the validated user input
# Description:
# This function prints the input prompt and gets user input.
# It verifies that the value from user input one of the two valid choices that
# are specified as parameters.
def get_choice(first,second,prompt): # define function
    ans = None #unacceptable value
    while ans is None or ans != first and ans != second: #while value of ans is None or it isn't equal to the first two parameters
        ans=input(prompt) #prompts user to change it to an acceptable value
    return(ans) #and returns it



# end of get_choice function


# STUDENT MUST WRITE THIS FUNCTION
# Function name: reveal_goat
# Funtction parameters:
#    int - The door with the prize
#    int - The door chosen by the user
# Returns: The number of a door that has a goat behind it
# Description:
# Chooses one of the doors that was not chosen by the user that has
# a goat behind the door. If the user chose the door with the prize, this
# method randomly chooses between the two remaining doors. If the user
# chose a door without the prize, this method returns the remaining door
# that does not have a prize.
def reveal_goat(prize,choice): #define function, below goes over all possible options for the parameters
    if prize == 1 and choice == 2 or prize == 2 and choice == 1:
        reveal = 3 # reveal is the value that will be returned
    if prize == 1 and choice == 3 or prize == 3 and choice == 1:
        reveal = 2
    if prize == 2 and choice == 3 or prize == 3 and choice == 2:
        reveal = 1
    if prize == 1 and choice == 1:
        reveal = random.randint(2,3)
    if prize == 3 and choice == 3:
        reveal = random.randint(1,2)
    if prize == 2 and choice == 2:
        preveal = random.randint(1,2) #to choose between 1 and 3 excluding 2
        if preveal == 1:
            reveal = 1
        else:
            reveal = 3
    return(reveal) #returns value
# End of reveal_goat function


# STUDENT MUST WRITE THIS FUNCTION
# Function name: get_remaining_door
# Funtction parameters:
#    int - The door chosen by the user
#    int - The door revealed by the host
# Returns: The number of the door not chosen by the user or revealed by the host
# Description:
# Returns the number of the door that was not chosen by the user
# and was not revealed by the host.

def get_remaining_door(chosen,revealed): #define function, returns value of 1 2 3 that was neither chosen nor revealed
    if chosen == 1 and revealed == 2 or chosen == 2 and revealed == 1:
        return(3)
    if chosen == 1 and revealed == 3 or chosen == 3 and revealed == 1:
        return(2)
    if chosen == 2 and revealed == 3 or chosen == 3 and revealed == 2:
        return(1)


# end of get_remaining_door function

######################################################################
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have completed the functions above, your functions must work with the
# code that is provided below.

# DO NOT MODIFY THIS FUNCTION
# Function name: play_interactive
# Description:
# Plays the Let's Make a Deal game in interactive mode
def play_interactive():

    # Randomly place the prize behind one of three doors
    prize_door = random.randint(1,3)

    # get the user's choice of a door
    user_door = get_int_range(0, 4, 'Choose a door (1, 2, or 3): ')

    # Host reveals a goat behind one of the doors not chosen by the user
    # then asks the user if they want to switch their door
    reveal_door = reveal_goat(prize_door, user_door)
    print('Behind door', reveal_door, 'is a goat...')
    remaining_door = get_remaining_door(user_door, reveal_door)
    print('Would you like to switch to door ' + str(remaining_door) + '?')
    switch_door = get_choice('y', 'n', 'Enter your choice (y/n): ')
    if switch_door == 'y':
        user_door = remaining_door

    # Show the user what they won
    print() # print a blank line
    if user_door == prize_door:
        print('Congratualtions!!!! You won a new car!!!!')
    else:
        print('Sorry, you won a goat :(')
        print('The prize was behind door', prize_door)
# End of play_interactive function

# DO NOT MODIFY THIS FUNCTION
# Function name: run_simulation
# Function parameter: integer - number of game instances to simulate
# Description:
# Runs many instances of the Let's Make a Deal game. Collects information
# about the game outcome and calculates statistics about all instances of the game.
def run_simulation(num_rounds):

    # Initialize variables for collecting information about the game outcome
    count_no_change = 0 # Counter for rounds when player did not change their door choice
    count_change = 0 # Counter for rounds when player changed their door choice
    win_no_change = 0 # Counter for wins when player did not change their door choice
    win_change = 0 # Counter for wins when player changed their door choice

    # Simulate num_rounds of the game
    for i in range(num_rounds):
        # Randomly place the prize behind one of the three doors
        prize_door = random.randint(1,3)

        # Randomly choose the player's door
        user_door = random.randint(1,3)

        # Host reveals a goat behind one of the doors not chosen by the player
        reveal_door = reveal_goat(prize_door, user_door)
        remaining_door = get_remaining_door(user_door, reveal_door)

        # Generate a random number to simulate the user choosing whether
        # or not to switch their door
        choice = random.random()
        if choice < 0.5:
            change_door = True
            user_door = remaining_door
            count_change += 1
        else:
            change_door = False
            count_no_change += 1

        # Determine if the player wins the prize
        if user_door == prize_door:
            # player won!
            if change_door:
                win_change += 1
            else:
                win_no_change += 1
    # End of for loop to simulate rounds of the game

    # Print the statistics
    print()
    print('--------------------')
    print('Simulated', num_rounds, "rounds of Let's Make a Deal")
    print('Player switched their door choice in', count_change, 'runs,')
    print('and won', win_change, 'of those runs.')
    print('Player did not switch their door choice in', count_no_change, 'runs,')
    print('and won', win_no_change, 'of those runs.')
    print()
    print('Percent of runs won when door was changed:' + str(100 * (win_change / count_change)) + '%')
    print('Percent of runs won when door was not changed:' + str(100 * (win_no_change / count_no_change)) + '%')
# End of run_simulation function

# DO NOT MODIFY THIS FUNCTION
# Function name: test_goat
# Function parameter: none
# Description:
# Tests the reveal_goat function by calling the function with all possible
# combinations of inputs. Prints an error message if the function returns
# an incorrect value.
def test_goat():
    random.seed(106)

    print('Testing the reveal_goat function')

    door = reveal_goat(1,1)
    if door != 3:
        print('\n***ERROR 1A door =', door)

    door = reveal_goat(1,2)
    if door != 3:
        print('\n***ERROR 1B door =', door)

    door = reveal_goat(1,3)
    if door != 2:
        print('\n***ERROR 1C door =', door)

    door = reveal_goat(2,2)
    if door != 1:
        print('\n***ERROR 1D door =', door)

    door = reveal_goat(2,1)
    if door != 3:
        print('\n***ERROR 1E door =', door)

    door = reveal_goat(2,3)
    if door != 1:
        print('\n***ERROR 1F door =', door)

    door = reveal_goat(3,3)
    if door != 2:
        print('\n***ERROR 1G door =', door)

    door = reveal_goat(3,1)
    if door != 2:
        print('\n***ERROR 1H door =', door)

    door = reveal_goat(3,2)
    if door != 1:
        print('\n***ERROR 1I door =', door)
    print('Finished reveal_goat test')
# end of test_goat function

# DO NOT MODIFY THIS FUNCTION
# Function name: test_door
# Function parameter: none
# Description:
# Tests the reveal_door function by calling the function with all possible
# combinations of inputs. Prints an error message if the function returns
# an incorrect value.
def test_door():
    random.seed(106)

    print('Testing the get_remaining_door function')

    door = get_remaining_door(1,2)
    if door != 3:
        print('\n***ERROR 2A door =', door)

    door = get_remaining_door(1,3)
    if door != 2:
        print('\n***ERROR 2B door =', door)

    door = get_remaining_door(2,1)
    if door != 3:
        print('\n***ERROR 2C door =', door)

    door = get_remaining_door(2,3)
    if door != 1:
        print('\n***ERROR 2D door =', door)

    door = get_remaining_door(3,1)
    if door != 2:
        print('\n***ERROR 2E door =', door)

    door = get_remaining_door(3,2)
    if door != 1:
        print('\n***ERROR 2F door =', door)

    print('Finished get_remaining_door test')
# end of test_door function


# DO NOT MODIFY THIS BLOCK OF CODE
# Main part of the program
# This is where the flow of execution begins when the program starts running
choice = get_int_range(0, 5, 'Enter 1 for interactive;\n      2 for simulation;\n      3 for reveal_goat test;\n      4 for get_remaining_door test: ')
if choice == 1:
    play_interactive()
elif choice == 2:
    print('How many rounds would you like in the simulation?')
    runs = get_int(0, 'Enter an integer greater than zero: ')
    run_simulation(runs)
elif choice == 3:
    test_goat()
elif choice == 4:
    test_door()
else:
    # The program should never run this code if the input validation is correct
    print('ERROR: incorrect choice of version')
