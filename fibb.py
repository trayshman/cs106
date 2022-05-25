
def fib_num(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        n2 = fib_num(n-2)
        n1 = fib_num(n-1)

        return n2 + n1

pos = int(input('enter a position for calculating fibonnaci: '))
print('calling the fib_num function')
f = fib_num(pos)

print('position',pos,'in the sequence is',f)
