n=0
total=0
while n<100:
    try:
        n_int+=int(n)

    except:
        print('no')
    n = input('enter an integer or done to stop: ')

print(total)
#dont put inputs inside try or else it will always except if 'done'
