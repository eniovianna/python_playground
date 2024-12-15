# -*- coding: utf-8 -*-
""""""

'''
File: if_then_else.py
Project: basics
Created Date: Saturday-June 20-06-2020 19:24:15
Author: Ênio Rodrigues Viana
Based on Youtube channel Socratica
-----
Last Modified: Saturday-June 20-06-2020 19:24:15
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
# Collect string / test length
string = input("Please enter a string: ")

if len((string)) < 6:
    print("Your string is too short!")
    print("Please enter a string with at leats 6 characters.")

# Prompt user to enter number / test if even or odd
number = input("Please enter a number: ")
number = int(number)
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same lengths.
# Equilateral triangle: All sides are equal.
a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))


if (a != b) and (b != c) and (a != c):
    print("This is a scalene triangle.")
elif a == b == c:
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")
