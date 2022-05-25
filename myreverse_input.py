#recursive functions are fucking stupid


def rev_string():
    word = input('Enter a word or type stop to "stop" entering input: ')

    if word == 'stop':
        #base case, do not ask for more input
        print('.... your words in reverse order .....')

    else:
        # recursive case
        # keep asking for input by making a RECURSIVE call to this function
        #print('Starting the recursive case')
        rev_string() #every call to the function is its own chunk of memory
        print(word)
         #dont need to use a list to print in reverse order



# end of rev_string function

# main part of the code
print('Calling the rev_string function')
rev_string()
