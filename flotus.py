in_file = open('mbox-short.txt')

# uct.ac.za

for a_line in in_file:
    if a_line.startswith('From:') and a_line.find('uct.ac.za') != -1:
        #print(a_line, end='')
        a_line = a_line.strip()
        print(a_line)

in_file.close()
