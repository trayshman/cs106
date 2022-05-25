# even_odd.py
# Author: Christine F. Reilly
# This program determines if the value input by the user is even or odd.

x = int(input('Enter an integer: '))

if x % 2 == 0:
    print(str(x) + ' is even')
else:
    print(str(x) + ' is odd')
print("this is the rest of the program")
