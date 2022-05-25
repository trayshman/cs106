# Your name: ryab

# CS106 Fall 2021
# Final Exam Take Home Problem 4 (6 points)
# f4_words.py: Complete the odd_words function

############################################################
# STUDENT MUST COMPLETE THIS FUNCTION
# Function name: odd_words
# Function parameter:
#    w_list - A list of strings
# Returns: The count of the number of strings in the list that have an odd number of letters.
# Description:
# This function uses recursion to count the nubmer of strings in a list that
# have an odd number of letters.
#
# Your task: Add to the code for the recursive case so that the function counts
# the number of words in the list that have an odd number of letters.
# You must use a recursive process for computing this count.
#
# Tip: this problem can be solved by adding between 2 and 4 lines of code.

def odd_words(w_list):

    if len(w_list) == 0:
        # Base case: reached end of list
        return 0
    else:
        # Recursive case
        count = odd_words(w_list[1:])

        # Beginning of where to add code
    if len(w_list)%2 !=0: #some sort of thing that finds odd numbers of letters in words
        return count


        # End of where to add code

        return count
# end of char_count function

# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.

# Main part of program

# The sample strings are from the quotes.txt file we used during the semester
s1 = 'bird watchers love fowl weather'
s1_list = s1.split()
c = odd_words(s1_list)
print(s1 + ':')
print(c, 'words with an odd number of letters')
print()

s2 = 'giraffes dine upstairs in the tree house'
s2_list = s2.split()
c = odd_words(s2_list)
print(s2 + ':')
print(c, 'words with an odd number of letters')
print()

s3 = 'Nothing is a waste of time if you use the experience wisely'
s3_list = s3.split()
c = odd_words(s3_list)
print(s3 + ':')
print(c, 'words with an odd number of letters')
print()

s4 = 'hello'
s4_list = s4.split()
c = odd_words(s4_list)
print(s4 + ':')
print(c, 'words with an odd number of letters')
print()

s5 = 'worlds'
s5_list = s5.split()
c = odd_words(s5_list)
print(s5 + ':')
print(c, 'words with an odd number of letters')
print()

s6_list = []
c = odd_words(s6_list)
print('(empty list)' + ':')
print(c, 'words with an odd number of letters')
