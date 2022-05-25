startDone = False
start=input('enter a starting point: ')
while not(startDone):
    try:
        start=int(start)
        startDone=True
    except:
        print('invalid input')
        start=input('enter a starting point: ')


stopDone = False
stop=input('enter a stopping point: ')
while not(stopDone):
    try:
        stop=int(stop)
        if stop>start:
            stopDone=True
        else:
            print('must be above starting point')
            stop=input('enter a stopping point: ')

    except:
        print('invalid input')
        stop=input('enter a stopping point: ')


count = 1
for j in range(start,stop+1):

    if count % 10 == 0:
        print(j)
    else:
        print(j, end = ' ')
    count+=1
