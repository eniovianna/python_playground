'''
Filename: c:\python_playground\basics\arithmetic.py
Path: c:\python_playground\basics
Created Date: Saturday, June 20th 2020, 6:44:10 pm
Author: Ênio Viana

Copyright (c) 2020 eniocc
Based on Socratica videos
'''


# Operations: + - * /

x = 28
y = 28.0
print(float(28))

pi = 3.14
print(int(pi))

Z = 2.00
print(type(Z))
Z += 0.32j
print(type(Z))

# The error below occurs because floats are narrower than complex numbers
# In other words, the complex numbers are widers than floats
#print(type(float(Z)))

a = 2       # int
b = 6.0     # float
c = 12 +0j  # complex number

# The rule is: Widen numbers so they're the same type

# Addition
print(type(a + b)) # int + float, results float

# Subtraction
print(type(b - a)) # float - int, results float

# Multiplication
print(type(a * 7)) # int * int, results int

# Division
print(type(c / b)) # complex / float, results complex

# Modulus
print (16 % 3)

# Exponent
print (a**b)

# Floor division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
print (9//2)
print (9.0//2.0)

# Floor division - But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity)
print(-11//3)
print(-11.0//3.0)