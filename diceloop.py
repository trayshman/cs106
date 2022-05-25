
#roll a 6 sided die 10 times

import random

sides = 6
rolls = 25
done = False #flag variable

while not(done):
    try:
        rolls = int(input('Enter number of rolls: '))
        done = True

    except:
        print('incorrect input, try again')


print('Using while loop to roll die')

# initialization
#sides and rolls initialized above
count = 0 #loop counter

#condition
while count < rolls:
    print('Roll',count, 'is a',random.randint(1,sides))

    count += 1


print('Using for loop to roll die')

for j in range(rolls):
    print('Roll',j, 'is a',random.randint(1,sides))
