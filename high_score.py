# high_score.py
# Author: Christine F. Reilly
# This program checks a player's score against the high score.

# Set the initial value of the high score
high_score = 1000

# Get the player's score from user input
player_score = int(input('What is your score? '))

# Compare the player's score with the high score. Update the high score if needed.
if player_score > high_score:
    print('You have the high score!')
    high_score = player_score

# Output the current high score
print('The high score is ', high_score)

# A note about this program: every time this program runs the high score will
# be set to the same initial value. After we learn about reading and writing
# data from/to files we could use a file to store the current high score
# and initialize the high score from that file.
