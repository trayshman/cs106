#Assignment 4
#Ryan Jones

import random #imports random

doneBal = False #flag for balance input
doneGame = False #flag for the program, when true, the game will end
bal=input('enter your balance, must be an integer that is greater than zero: $') #input for the user's money balance
while not (doneBal): #while a successful balance input has not been entered
    try:

        bal=int(bal) #check that it's an integer
        if bal>0: #as well as greater than 0
            doneBal = True #successful balance has been entered
        else:
            print("Your balance can't be negative or zero dollars") #yells at user for entering a value of zero, or negative dollars
            bal=input('enter your balance, must be an integer that is greater than zero: $') #re-prompts the user to enter a correct balance
    except: #integer not entered
        print('incorrect input, try again')
        bal=input('enter your balance, must be an integer that is greater than zero: $') #re-prompt



while bal>0 and not(doneGame): #while the balance is more than 0 and the game is not done
    doneGuess=False #initializes doneGuess as false
    doneBet = False #initializes doneBet as false
    bet=input('Enter a bet that is a whole number, greater than zero, and less than or equal to your balance: $') #bet prompt
    while not(doneBet): #while a valid bet has not been entered
        try:
            bet=int(bet) #must be an integer
            if bet>0 and bet<=bal: #that is greater than 0 and less than the balance
                doneBet = True #then a successful bet has been entered and we can proceed
            else:
                print("You can't bet zero or negative dollars, or go above your balance!") #yells at user for trying to input an integer that is 0 or less, or greater than the balance
                bet=input('Enter a bet that is a whole number, greater than zero, and less than or equal to your balance: $') #re-prompt

        except:
            print('incorrect input, try again') #not an integer
            bet=input('Enter a bet that is a whole number, greater than zero, and less than or equal to your balance: $')





    guess=input('What dice side will appear? Enter a number from 1 to 6: ') #guess prompt
    while not(doneGuess): #while a valid dice guess has not been entered
        try:
            guess=int(guess) #must be an integer
            if guess>=1 and guess<=6: #must be between 1 and 6 (inclusive)
                doneGuess = True #valid dice guess inputted
            else:
                guess=input('What dice side will appear? Enter a number from 1 to 6: ') #otherwise re-prompt

        except:
            guess=input('What dice side will appear? Enter a number from 1 to 6: ') #otherwise re-prompt


    print('Rolling dice.............')
    rolls=3 #amount of rolls of dice that will happen
    payout=0 #variable in determining how much you won

    for roull in range(rolls): #for loop
        roull=random.randint(1,6) #rolls random number between 1 and 6 (inclusive)
        if roull==guess: #checks if your number came up
            payout+=1 #every time your number comes up, this goes up by 1
        print(roull,end=' ') #displays the roll

    if payout==0: #if you won nothing
        print(' ')
        print('Sorry, better luck next time') #offers condolences
        bet=int(bet) #initializes bet as an integer because it was a string
        bal-=bet #and subtracts it from your balance
    else:
        print(' ')
        prize=int(bet*payout) #prize is how much you just won
        print('You won $',prize) #prints how much you won
        bal+=prize #adds how much you won to your balance
    print('new balance is: $',bal) #displays your new balance

    if bal<=0: #if you're broke
        print("You're out of cash")
        doneGame = True #ends the game
    if not doneGame: #while the game hasn't ended
        doneQuit=False #flag for if you quit the game
        while not doneQuit: #while  you haven't quit
            try:
                quit=input('do you want to quit, enter yes if so, or no to continue: ') #now is your chance to quit
                if quit=='yes' or quit=='Yes': #yes, you are quitting
                    doneGame=True #so game end
                    doneQuit=True #you correctly answered if you wanted to quit or not
                if quit=='no' or quit=='No': #no, you want to continue playing
                    doneGame=False #game not end
                    doneQuit=True #you correctly answered if you wanted to quit or not
            except:
                doneQuit=False #you didn't correctly answer the prompt
if doneGame == True: #the game will now end
    print('game end') #bye bye
