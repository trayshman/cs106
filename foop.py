def get_choice(first,second,prompt):
    ans = None
    while ans is None or ans != first and ans != second:
        ans=input(prompt)
    return(ans)


switch_door = get_choice('y', 'n', 'Enter your choice (y/n): ')
print(switch_door)
