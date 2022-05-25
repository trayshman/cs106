

#for i in range(0,100,3):
#    print(i,end=' ')


def letter_idx(x,y):
    x=x.lower()
    y=y.lower()
    count=-1
    for i in x:
        count+=1
        if y == i:
            print(count)


letter_idx('NovEmber','E')
