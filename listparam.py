#example 2: create a function to delete an item from a list and return the item
#function parameter t is a list
def delete_index(t):
    print('valid list indexes are 0 through',len(t)-1)
    i = int(input('What index to delete from? '))
    x = t.pop(i)
    return(x)
