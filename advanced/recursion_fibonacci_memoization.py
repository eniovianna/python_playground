# -*- coding: utf-8 -*-
""""""
'''
File: recursion_fibonacci_memoization.py
Project: advanced
Created Date: Thursday-July 2-07-2020 22:59:14
Author: Ênio Rodrigues Viana
-----
Last Modified: Thursday-July 2-07-2020 22:59:14
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on Sovcratica Youtube channel
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""


from functools import lru_cache
import time
VALUE_TEST = 30

def fibonacci(n):
    """Return the value of n-th position. Unfortunately, this method
    run very slow for increasing numbers. Explanation here https://youtu.be/Qk0zUZW-U_M?t=190"""
    # Check that the input is a positive integer
    if (type(n) != int):
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int or zero")

    # Compute the n-th term
    if n == 0:
        # Position 0
        return 0
    return 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


# Uncomment the lines below to test example
"""
#### Example begins here

time_start = time.time()
for i in range(VALUE_TEST):
    print("element {0} - value {1}".format(i, fibonacci(i)))
time_end = time.time()
print("Evaluated time: {0}".format(time_end-time_start))
print(64*'=')

#### Example end here
"""
# A simple to solve this is using Memoization. Python has two way to do that:
# 1 - Implement explicity
# 2 - Use builtin Python tool

fibonacci_cache = {}


def fibonacci_(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Check that the input is a positive integer
    if (type(n) != int):
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int or zero")
    
    # Compute the n-th term
    if n == 0:
        # Position 0
        value = 0
    if n == 1:
        value = 1
    elif n > 1:
        value = fibonacci_(n - 1) + fibonacci_(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


# Uncomment the lines below to test example
"""
#### Example begins here

time_start = time.time()
for i in range(VALUE_TEST):
    print("element {0} - value {1}".format(i, fibonacci_(i)))
time_end = time.time()
print("Evaluated time: {0}".format(time_end - time_start))

#### Example end here
"""

@lru_cache(maxsize = 1000)
def fibonacci_lru(n):
    # Check that the input is a positive integer
    if (type(n) != int):
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int or zero")

    # Compute the n-th term
    if n == 0:
        # Position 0
        return 0
    return 1 if n == 1 else fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# Uncomment the lines below to test example
"""
#### Example begins here

time_start = time.time()
for i in range(VALUE_TEST):
    print("element {0} - value {1}".format(i, fibonacci_lru(i)))
time_end = time.time()
print("Evaluated time: {0}".format(time_end - time_start))

#### Example end here
"""

time_start = time.time()
fibonacci(VALUE_TEST)
print("Tempo: {0}".format(time.time()-time_start))

time_start = time.time()
fibonacci_(VALUE_TEST)
print("Tempo: {0}".format(time.time()-time_start))

time_start = time.time()
fibonacci_lru(VALUE_TEST)
print("Tempo: {0}".format(time.time()-time_start))