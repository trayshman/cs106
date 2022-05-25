
cs_profs = ['Eckmann', "O'Connell", 'Prasad', 'Read', 'Reilly']

values = [123.45, 678.9, 987.654]

# Example 1: print names of CS professors
print('The CS professors are:')

for name in cs_profs:
    print('Professor',name)

print('\n\nSome of the profs: ')

for i in range(2, 5):
    print('Professor',cs_profs[i])
