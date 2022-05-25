

#parameters:
# vals: the list that we're Searching
# key: the value to search for
# startpos: the starting position in the list  (start of part of list to search)
# endpos: the ending position in the list (end of part of the list to search )


def binary_search(vals,key,startpos,endpos):


    # calculate the middle position of the list
    # this finds the index in the list vals for the middle position
    middle = (startpos + endpos) // 2 #dont forget to use integer division '//' rather than regular '/' so it doesn't return a float

    if key == vals[middle]:
        # base case 1: found the key in the list
        # return the index where the key is found
        return middle
    elif key < vals[middle]:
        # key comes earlier in the list
        # change end position so only the earlier part of the list will be searched
        endpos = middle - 1
    else:
        # key comes later in the list
        # change the start position so only the later part of the list will be searched
        startpos = middle + 1


    if startpos <= endpos:
        # There are more values in the list to search
        # Recursively call this binary search function to continue the search
        return binary_search(vals,key,startpos,endpos)
    else:
        # base case 2: no more list items to check
        # key is not in this list
        return -1



animals = ['ant', 'caterpillar', 'elephant', 'gorilla', 'salamander', 'shark', 'spider', 'walrus', 'white tail deer']
numbers = [-458, -448, -445, -437, -427, -425, -421, -379, -373, -372, -359, -343, -334, -326, -317, -287, -282, -261, -249, -239, -224, -222, -190, -171, -132, -80, -39, -31, -11, 8, 22, 41, 46, 51, 64, 75, 89, 96, 102, 112, 179, 224, 236, 250, 261, 276, 300, 337, 422, 463]


# For binary search, startpos is 0 and endpos is the last index
print('Searching animals')
pos = binary_search(animals, 'spider', 0, len(animals)-1)
print('Binary search found key at position', pos)

# For binary search, startpos is 0 and endpos is the last index
print('\nSearching numbers')
pos = binary_search(numbers, -317, 0, len(numbers)-1)
print('Binary search found key at position', pos)

print('\nStarting exercise example:')
exercise = [1, 2, 5, 13, 17, 18, 24, 27, 28, 29]
pos = binary_search(exercise, 18, 0, len(exercise)-1)
print('Binary search found key at position', pos)
