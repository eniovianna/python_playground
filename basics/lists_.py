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
Based on Socratica Youtube channel
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
# A simple list definition
example = list()
print(example)
print(type(example))
# Another simple definition
example = []
print(example)
print(type(example))
# And another way
primes = [2, 3, 5, 7, 11, 13]
# To add more items
primes.append(17)
primes.append(19)
print(primes)
# To acces items, be carefull with bounds errors
print(primes[1])
print(primes[-1])
# Let's see slices. Slices includes start index but exclude the end index
print(primes[2:5])
# List could be have different types, including another lists
example = [128, True, "Alpha", 1.732, [64, False]]
print(example)
# In lists we can repeat the elements.
dice_rolls = [1, 2, 6, 6, 4, 3, 4]
print(dice_rolls)
# We can combine lists, order matter
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(numbers + letters)
print(letters+numbers)
# Let's see possible methods to a list
print(help(letters))
letters.sort()
print(letters)