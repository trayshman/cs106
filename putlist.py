a = [] #initialize as empty list

fhand = open('num.txt')


# read each number from the input file (one integer per line)
# put each number into a

for line in fhand:
    a.append(int(line))

# end of reading file

print('1: contents of list:')
print(a)



for i in range(3):
    s = input('enter a string: ')
    a.append(s)

print('2: contents of list:')
print(a)



#example 2: create a function to delete an item from a list and return the item
#function parameter t is a list
def delete_index(t):
    print('valid list indexes are 0 through',len(t)-1)
    i = int(input('What index to delete from? '))
    x = t.pop(i)
    return(x)


del_item = delete_index(a)
print('deleted item:', del_item)
print('after example 2 contents of list:')
print(a)
