# -*- coding: utf-8 -*-
""""""
'''
File: 4_constructors.py
Project: python_playground
Created Date: Tuesday-July 7-07-2020 15:17:31
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:17:31
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on https://www.programiz.com/python-programming/object-oriented-programming
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# Uncomment line below to see the error
# print(num1.attr) # AttributeError: 'ComplexNumber' object has no attribute 'attr'

"""
Deleting Attributes and Objects
Any attribute of an object can be deleted anytime, using the del statement. Try the following on the Python shell to see the output.
"""
num1 = ComplexNumber(2, 3)

del num1.imag
# Uncomment the code below to see the error
# print(num1.get_data()) # Traceback (most recent call last): AttributeError: 'ComplexNumber' object has no attribute 'imag'

del ComplexNumber.get_data
# Uncomment the code below to see the error
# print(num1.get_data()) # Traceback (most recent call last): AttributeError: 'ComplexNumber' object has no attribute 'get_data'

# We can even delete the object itself, using the del statement.
c1 = ComplexNumber(1,3)
del c1

# The code below will generate an error. Uncomment to see.
# print(c1) # Traceback (most recent call last): NameError: name 'c1' is not defined
