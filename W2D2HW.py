# Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]
# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]
def lessThan(lst):
    lst2 = []
    for i in range(len(lst)):
        if lst[i] < 10:
            lst2.append(lst[i])
    return lst2

print(lessThan(l_1)) # Testing lessThan function

# Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def mergeSorted(ls1, ls2):
    for i in range(len(ls2)):
        ls1.append(ls2[i])
    ls1.sort()
    return ls1

print(mergeSorted(l_1,l_2)) # Testing mergeSorted() function

