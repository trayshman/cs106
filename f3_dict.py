# Your name: Ryan

# CS106 Fall 2021
# Final Exam Take Home Problem 3 (12 points)
# f3_dict.py: Complete the tasks as instructed.

############################################################
# TASK 1 (3 points):
# Read words from a file and count the number of characters in each word. Use
# a dictionary to keep track of the number of words that have each letter count,
# where the key is the number of letters per word and the value is the count of
# words that have that number of letters.

fhand = open('words.txt')

# Write your code for Task 1:
a=dict()
for line in fhand:
    line = line.strip()
    line = line.split()
    for c in line:
        if len(c) not in a:
            a[len(c)] = 1
        else:
            a[len(c)] +=1


# NOTE: For Tasks 2 and 3, if you did not complete Task 1 you may use the following dictionary
# stuff = {6:23, 4:8, 1:7, 5:67, 2:39, 3:43}

############################################################
# TASK 2 (4 points):
# Print the dictonary sorted in descending order by the number of letters per
# word (the dictionary key).
print('Task 2:')
# Write your code for Task 2:
key_list = list(a.keys())


key_list.sort(reverse=True) # Sort the list of keys in reverse

for k in key_list:
    # Print the key and its associated value from the dictionary
    print(k,'letters: ', a[k],'words')


############################################################
# TASK 3 (5 points):
# Print the dictonary sorted in ascending order by the number of words with
# each letter count (the dictionary value). When there are multiple letter counts
# that have the same number of words, the order within that letter count does
# not matter. It is possible that your output may not exactly match the sample
# output in this case.
print('\nTask 3:')
# Write your code for Task 3:
vk=[]
for key, val in list(a.items()):
    # add a tuple to the value-key list
    vk.append( (val, key) )

vk.sort()

for key,val in vk:
    # Print the key and its associated value from the dictionary
    print(key,'words: ', val,'letters')
#val_list = list(a.values())

#val_list.sort() # Sort the list of keys

#for v in val_list:
    #print(v) #i dont know how to sort and print by values, and i couldnt find anything in the spring that says how to
