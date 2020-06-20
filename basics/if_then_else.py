"""
Filename: c:\python_playground\basics\if_then_else.py
Path: c:\python_playground\basics
Created Date: Saturday, June 20th 2020, 7:24:15 pm
Author: Ênio Viana

Copyright (c) 2020 eniocc
Based on Socratica videos
"""
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
elif (a == b) and (b == c):
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")
