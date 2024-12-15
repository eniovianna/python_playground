# -*- coding: utf-8 -*-
""""""

'''
File: lists_.py
Project: basics
Created Date: Saturday-July 4-07-2020 17:56:28
Author: Ênio Rodrigues Viana
-----
Last Modified: Saturday-July 4-07-2020 17:56:28
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on Socratica Youtube channel  and https://www.programiz.com/python-programming/list
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
05-07-2020
'''
""""""
# A simple list definition
example = []
print(example)
print(type(example))
# Another simple definition
example = []
print(example)
print(type(example))
# And another way
primes = [2, 3, 5, 7, 11, 13]

# To acces items, be carefull with bounds errors
print(primes[1])
print(primes[-1])

# Let's see slices. Slices includes start index but exclude the end index
print(primes[2:5])
print(primes[:5])
print(primes[2:])
print(primes[:])

# List could be have different types, including another lists (nested lists)
example = [128, True, "Alpha", 1.732, [64, False]]
print(example)
# We can access nested lists
print(example[-1][1])

# In lists we can repeat the elements.
dice_rolls = [1, 2, 6, 6, 4, 3, 4]
print(dice_rolls)

# We can combine lists, order matter
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters+numbers)

# To change a element in a list is simple
odd = [2, 4, 6, 8]
odd[0] = 1  # change the 1st item
print(odd)
odd[1:4] = [3, 5, 7]  # change 2nd to 4th items
print(odd)

# Let's see possible methods to a list
print(help(letters))
letters.sort()
print(letters)

primes.extend((17, 19))
print(primes)

# To remove items
del primes[-1]
del primes[-1]
print(primes)

# Deleting multiple items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete multiple items
del my_list[1:5]
print(my_list)

# Another way to add items
primes.extend([17, 19])
print(primes)

# We can insert an item in a specific location
odd = [1, 9]
odd.insert(1, 3)
print(odd)
odd[2:2] = [5, 7]
print(odd)

# Deleting a entire list
del odd # If we try print this list or do another operation we will receive a error

# To remove the given item we can use remove() or pop()
my_list = ['p','r','o','b','l','e','m']
print(my_list)

my_list.remove('p')
print(my_list)

print(my_list.pop(1))
print(my_list)

print(my_list.pop())
print(my_list)

# We can clear the list without remove it
my_list.clear()
print(my_list)

# There are a lot of methods in list
"""
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of the number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
"""

# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8)) # Output: 1
print(my_list.count(8)) # Output: 2
my_list.sort()
print(my_list) # Output: [0, 1, 3, 4, 6, 8, 8]
my_list.reverse()
print(my_list)  # Output: [8, 8, 6, 4, 3, 1, 0]

# List Comprehension: Elegant way to create new List
pow2 = [2 ** x for x in range(10)]
print(pow2)

# List membership test
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print('p' in my_list) # Output: True
print('a' in my_list) # Output: False
print('c' not in my_list)  # Output: True

# Iterating through a list
for fruit in ['apple','banana','mango']:
    print("I like",fruit)