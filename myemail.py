
dir=dict()

fhand = open('emails.txt')


#read input file, put entries into dictionary
for line in fhand:
    # strip leading and trailing whitespace
    # split into pieces using space as delimiter
    pieces = line.strip().split()

    # create tuple (last name, first name)
    k = (pieces[1], pieces[0])

    # add key to dictionary with the value email address
    dir[k] = pieces[2]
# end of loop that reads file and creates dictionary

# print dictionary, sorted by last name
key_list = list(dir.keys()) # makes list of keys in the dict
key_list.sort()


for last, first in key_list:
    print(last +", "+ first + ': ' + dir[last,first])



# ask user for first and last name
# print the associated email address
print('\nLookup an email address')

first = input('Enter first name: ')
last = input('Enter last name: ')

# lookup the email address

email = dir[last, first]
print('email: ',email)
