def load_customer(fname):
    a=[] #empty list
    f_read=open(fname) # open the file
    for line in f_read: #for each line in the file
        good_line=line.strip() #strip of all whitespace
        parts=good_line.split('|') #and split based on when | shows up in the line
        a.append(parts) # and add all those split parts to the empty list

    return a #and return it



a=load_customer('cust.txt')

print(a)
