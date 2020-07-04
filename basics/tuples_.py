# -*- coding: utf-8 -*-
""""""
'''
File: lists_.py
Project: basics
Created Date: Thursday-July 2-07-2020 23:59:49
Author: Ênio Rodrigues Viana
-----
Last Modified: Thursday-July 2-07-2020 23:59:49
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
# Tuple and List declaration is the same
import timeit
import random
import sys
list_example = [0, 1, 2, 3, 4]
tuple_example = (0, 1, 2, 3, 4)

# Tuple and List iteration is the same
for l in list_example:
    print(l)
print(64*"=")

for t in tuple_example:
    print(t)

TEST_SIZE = 100


# Create a random tuple
list_int = []
tuple_int = [random.randint(0, 1) for i in range(TEST_SIZE)]
# After this point the tuple can not be modify becayse it is immutable.
# The lists are mutable

# Create a random list.
for i in range(TEST_SIZE):
    list_int.append(random.randint(0, 1))
    # After this point we can modify the list. Lists are mutable.

print("LIST\t\tTUPLE")
for i in range(TEST_SIZE):
    # We can iterate lists and tuples with a simple for
    print("{0}\t\t{1}".format(list_int[i], tuple_int[i]))

print("\tLENGTH")
print("LIST\t\tTUPLE")
# A bad point in lists is the size, look the difference below.
# In some cases, like big data, tuple is a good alternative to reduce size in memory.
list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)
print("{0}\t\t{1}".format(sys.getsizeof(list_eg), sys.getsizeof(tuple_eg)))


# Now we will check the time to create 1 million lists and tuples
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("\tTIME")
print("LIST\t\tTUPLE")
print("{:.8f}\t{:.8f}".format(list_test, tuple_test))

# Create a empty tuple
empty_tuple = ()
test1 = ("a")
test2 = ("a", "b")
test3 = ("a", "b", "c")
print(test1)  # Here the print is just a, without sigle quotes
print(test2)
print(test3)
# We can see that tuple is not a tuple, is a string. See below to fix this
print(type(test1))
print(type(test2))
print(type(test3))

empty_tuple = ()
test1 = ("a", )
test2 = ("a", "b")
test3 = ("a", "b", "c")
print(test1)  # Here the print is 'a', with sigle quotes
print(test2)
print(test3)
print(type(test1))  # We can see that tuple is a tuple now
print(type(test2))
print(type(test3))


# Let's see an alternative way to create tuples
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3
print(type(test1))
print(type(test2))
print(type(test3))

# Let's see tuple assignment and it access
# (age, country, knows_python), it is our tuple model
survey = (27, "Vietnam", True)
# Access
age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age = ", age)
print("Country = ", country)
print("Knows Python = ", knows_python)

# Other simple way to access value in a tuple
survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age = ", age)
print("Country = ", country)
print("Knows Python = ", knows_python)

# Be carefull
country = ("Australia")
print(country)  # We are printing a string
country = ("Australia",)
print(country)  # We are printing a tuple

# Be sure that the number of variables match with the number of elements assigned.
# See the line bellow. Uncomment to test.
# a, b, c = (1, 2, 3, 4)  # In this case we have more elements than variables

# Similar occurs below when the number of variables is greater than elements in tuple
# x, y, z = (1, 2)
