#simulate a random coin toss

import random # use the random module
random.seed(106) #same random numbers each time
#using random.random()

print('Using random.random()')

toss1=random.random()
print('toss1 = ', toss1)
if toss1 < 0.5:
    print('HEADS')
else:
    print('TAILS')

print('Using random.randint()')

toss2=random.randint(1,2)
print('toss2 = ', toss2)
if toss2 == 1:
    print('HEADS')
else:
    print('TAILS')
