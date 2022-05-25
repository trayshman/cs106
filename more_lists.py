# more_lists.py
# Author: Christine F. Reilly
# Demonstration of copying a list and lists of lists

import copy

##### Example 1: Copying a list
print('Example 1: Copying a list')
a = [49, 16, 43]

# Use the copy method to create a copy of list a
b = a.copy()
print('list a:', a)
print('list b is a copy of a:', b)

# confirm that the two lists are different objects
# When we change one list, the other is not changed
a[0] = 123
print('changed first element of list a:', a)
print('list b:', b)
b[2] = 987
print('changed last element of list b:', b)
print('list a:', a)

print() # print a blank line

# Use slice notation to create a copy of list a
c = a[:]
print('list a:', a)
print('list c is a copy of a:', c)

# confirm that the two lists are different objects
# When we change one list, the other is not changed
a[1] = 357
print('changed second element of list a:', a)
print('list c:', c)
c[0] = 654
print('changed first element of list c:', c)
print('list a:', a)

##### Example 2: A list that contains lists
print('\n\nExample 2: A list that contains lists')
t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('list t contains lists:', t)

print('\nusing nested loop with indexes to print list t as a table')
# Use nested loops to iterate over each item in the list of lists
# Outer loop: iterate over the rows
for i in range(len(t)):
    # Inner loop: iterate over each column in the row
    for j in range(len(t[i])):
        print(t[i][j], end=' ')
    # After the inner loop, print an end of line
    print()
# After the outer loop

print('\nusing nested loop with variable to print list t as a table')
# Use nested loops to iterate over each item in the list of lists
# Outer loop: iterate over the rows
for row in t:
    # Inner loop: iterate over each column in the row
    for col in row:
        print(col, end=' ')
    # After the inner loop, print an end of line
    print()
# After the outer loop

# Example 3: shallow copy
print('\n\nExample 3: Shallow copy')
r = t.copy() # r is a shallow copy of t
print('list t:', t)
print('list r is a shallow copy of t:', r)

# When we change an element inside one of the inner lists, both outer lists are changed
t[0][0] = 123
print('\nchanged element [0][0] of list t:', t)
print('list r:', r)
r[2][2] = 987
print('\nchanged element [2][2] of list r:', r)
print('list t:', t)

# Lists t and r are different objects. If we change the lists that t contains,
# r is not changed
t[0] = [98, 76, 54]
print('\nchanged element [0] of list t:', t)
print('list r:', r)

# Example 4: deep copy
print('\n\nExample 4: Deep copy')
# Note: the copy module is imported at the top of this file
q = copy.deepcopy(t)
print('list t:', t)
print('list q is a deep copy of t:', q)

# When we change an element inside one list, the other list is not changed
t[0][0] = 111
print('\nchanged element [0][0] of list t:', t)
print('list q:', q)
q[2][2] = 555
print('\nchanged element [2][2] of list q:', q)
print('list r:', r)
