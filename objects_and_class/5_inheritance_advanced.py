# -*- coding: utf-8 -*-
""""""
'''
File: 5_inheritance_advanced.py
Project: python_playground
Created Date: Tuesday-July 7-07-2020 15:30:10
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:30:10
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
https://www.programiz.com/python-programming/inheritance
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""

"""
Python Inheritance Syntax

class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class

Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
"""


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)} : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()

t.inputSides()

t.dispSides()

t.findArea()

print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))

print(issubclass(Polygon,Triangle))
print(issubclass(Triangle,Polygon))
print(issubclass(bool,int))