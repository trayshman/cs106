
# vals: the list of values to search
# key: the data we are looking for
# assume there are no duplicates in vals
def linear_search(vals, key):
    for i in range(len(vals)): # for i in the entirety of vals
        if vals[i] == key:
            # found the key!
            # return the index where the key is located in the list
            return i
    # end of loop through list
    # if program reaches this point, key is not in the vals list
    return -1




animals = ['ant', 'caterpillar', 'elephant', 'gorilla', 'salamander', 'shark', 'spider', 'walrus', 'white tail deer']
numbers = [-458, -448, -445, -437, -427, -425, -421, -379, -373, -372, -359, -343, -334, -326, -317, -287, -282, -261, -249, -239, -224, -222, -190, -171, -132, -80, -39, -31, -11, 8, 22, 41, 46, 51, 64, 75, 89, 96, 102, 112, 179, 224, 236, 250, 261, 276, 300, 337, 422, 463]

print('Searching animals')
pos = linear_search(animals, 'spider')
print('Linear search found key at position', pos)


print('\nSearching numbers')
pos = linear_search(numbers, -317)
print('Linear search found key at position', pos)

print('\nSearching numbers')
pos = linear_search(numbers, 1)
print('Linear search found 1 at position', pos)
