numbers = [69,21,42,84,93,2,7,9,224,0,5]
x = numbers[0]

print(x)


str_list=['the','what','why','help']

str_list.append('bye')

print(str_list)

table = [[13,64,7,32,54],[87,3,74,99,86],[24,75,25,65,12]]

table[1][3]=4

print(table)

for i in range(len(numbers)):
    if numbers[i]<10:
        numbers[i]=10

numbers.sort()

print(numbers)



outer=[]
for row in range(1000):
    inner=[]
    for col in range(100):
        inner.append(col)
    outer.append(inner)


#print in a less messy way
for row in outer:
    for col in row:
        print(col,end=' ')

print()
d = {'a':123, 'b':456, 'c':789}

done=d['b']
print(done)


def rec_prob(x):
    print('x =', x)
    if x > 0:
        return x + rec_prob(x-1)
    else:
        return x
# end of rec_prob function

# Main part of program
y = rec_prob(3)
print('y =', y)
