# -*- coding: utf-8 -*-
""""""

'''
File: sets_.py
Project: basics
Created Date: Monday-July 6-07-2020 22:00:16
Author: Ênio Rodrigues Viana
-----
Last Modified: Monday-July 6-07-2020 22:00:16
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on Socratica Youtube channel and https://www.programiz.com/python-programming/set
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
# Empty example
example = set()
print(example)
print(dir(example))

# Let's add some items in our set
example.add(33)
example.add(True)
example.add("He")
example.add(3.14159)
print(example)  # Pay attention to print order. In sets, order doesn't matter.
# If we try to add the same element in a set nothing will happen, set's doesn't duplicate elements
example.add(42)
print(example)
print(len(example))

# To remove an element in a set
example.remove(42)
print(example)
print(len(example))

# If we try to remove an element that is not in set we will receive an error
# Uncomment the lines below tho see how to it works
"""
example.remove(42)
print(example)
"""

# To avoid the error above we can use discard method
example.discard(42)
print(example)
# We can start a set starts from a list
example2 = {1, True, 'Europe', 2.71828}
print(len(example2))

# Let's clear our set
example2.clear()
print(example)

# If we have 2 sets, the combination of all elements from the two sets is denoted with Union
# The intersection is the set of elements inside both A and B sets
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}
# composite integers - the integers which can be factored
composites = {4, 6, 8, 9, 10}

print(odds.union(evens))
print(evens.union(odds))
print(odds.intersection(primes))
print(evens.intersection(primes))
print(evens.intersection(odds))
print(primes.union(composites))

# Let's check if a number is (or not) in a set
print(2 in primes)
print(6 in odds)
print(9 not in evens)
