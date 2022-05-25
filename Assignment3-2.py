#Assignment 3
#Ryan Jones

import random #import random
doneBet = False # Yeah, we're doing flag variables this time. Flag for the player's bet

bet=input('Enter a bet that is a whole number and greater than zero: $') #the player's bet
while not(doneBet): #until you enter the correct input this will repeat
    try:

        bet=int(bet) #number has to be an integer
        if bet>0: #and greater than 0
            doneBet = True #makes it so it doesn't repeat the whole thing anymore
        else:
            print("You can't bet zero or negative dollars!") #yells at user for trying to input an integer that is 0 or less
            bet=input('Enter a bet that is a whole number and greater than zero: $') #prompts user again to enter a correct variable

    except:
        print('incorrect input, try again')
        bet=input('Enter a bet that is a whole number and greater than zero: $') #prompts user again to enter a correct variable


doneGuess=False #Flag variable for guess

guess=input('What dice side will appear? Enter a number from 1 to 6: ')
while not(doneGuess): #will repeat until correct integer inputted, between 1 and 6
    try:
        guess=int(guess) #must be an integer
        if guess>=1 and guess<=6: #must be between 1 and 6, including 1 and 6
            doneGuess = True #end of the loop
        else:
            guess=input('What dice side will appear? Enter a number from 1 to 6: ') #try again
    except:
        guess=input('What dice side will appear? Enter a number from 1 to 6: ') #try again


print('Rolling dice.............')
rolls=3 #changeable number of rolls, the problem says to use a for loop and to use 3 loops
payout=0 #variable in determining how much you won

for roull in range(rolls): #for loop
    roull=random.randint(1,6) #rolls a random number between 1 and 6, including 1 and 6
    if roull==guess: #checks if your number came up
        payout+=1 #every time your number comes up, this goes up by 1
    print(roull) #displays the roll

if payout==0: #offers condolences if you won nothing
    print('Sorry, better luck next time')
else:
    print('You won $',(bet*payout)) #multiplies your bet based on how many times your guess came up
