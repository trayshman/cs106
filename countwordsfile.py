
in_file = open('aroundWorld.txt', 'r')
count_of_words = 0

for a_line in in_file:
    good_line = a_line.strip()
    print(good_line)
    words = good_line.split()
    count_of_words += len(words)

in_file.close()
print('the number of words in the file is',count_of_words)
