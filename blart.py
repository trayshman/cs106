

list= [3, 41, 12, 9, 74, 15]
largest=list[0]
print('Before:',largest)

for itervar in list:
    if itervar > largest:
        largest = itervar
    print('Loop:', itervar, largest)


print('Largest:', largest)
