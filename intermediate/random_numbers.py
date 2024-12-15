# -*- coding: utf-8 -*-
""""""

'''
File: random_numbers.py
Project: intermediate
Created Date: Tuesday-June 30-06-2020 17:18:01
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-June 30-06-2020 17:18:1
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on Youtube Channel Socratica
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""


# Functions available in this module
import random
print(dir(random))

# Print help for random function
print(help(random.random))

# Display 10 random numbers between 0 and 1
for _ in range(10):
    print(random.random())

# Generate random numbers from interval 3-7. Way #0


def my_random():
    # Random, scale, shift, return
    return 4 * random.random() + 3


# Print 10 random numbers from call function my_random()
for _ in range(10):
    print(my_random())


# Generate random numbers from interval 3-7. Way #1 (uniform function)
print(help(random.uniform))
for _ in range(10):
    print(random.uniform(3, 7))

# Generate random numbers from a Gaussian Distribution
print(help(random.normalvariate))
for _ in range(10):
    print(random.normalvariate(0, 10))

# Generante random int numbers
print(help(random.randint))
for _ in range(10):
    print(random.randint(0, 9))

# Generate from a random from a list
outcomes = ['rock', 'paper', 'scissor']
for _ in range(10):
    print(random.choice(outcomes))
