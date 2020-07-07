# -*- coding: utf-8 -*-
""""""
'''
File: 7_operator_overloading.py
Project: objects_and_class
Created Date: Tuesday-July 7-07-2020 16:34:56
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 16:34:56
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
https://www.programiz.com/python-programming/operator-overloading
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        # What actually happens is that, when you use p1 + p2, Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2).
        # After this, the addition operation is carried out the way we specified.
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __lt__(self, other):
        # Let us compare the magnitude of these points from the origin and return the result for this purpose. It can be implemented as follows.
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = Point(1, 2)
print(p1)
p2 = Point(2, 3)
print(p2)
# It will generate an error, at least that we have an operator overloading to (+)
print(p1+p2)

"""
Similarly, we can overload other operators as well. The special function that we need to implement is tabulated below.

Operator	            Expression	Internally
Addition	            p1 + p2	    p1.__add__(p2)
Subtraction	            p1 - p2	    p1.__sub__(p2)
Multiplication	        p1 * p2	    p1.__mul__(p2)
Power	                p1 ** p2	p1.__pow__(p2)
Division	            p1 / p2	    p1.__truediv__(p2)
Floor Division	        p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	    p1 % p2	    p1.__mod__(p2)
Bitwise Left Shift	    p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	    p1 >> p2	p1.__rshift__(p2)
Bitwise AND	            p1 & p2	    p1.__and__(p2)
Bitwise OR	            p1 | p2	    p1.__or__(p2)
Bitwise XOR	            p1 ^ p2	    p1.__xor__(p2)
Bitwise NOT	            ~p1	        p1.__invert__()
"""


# Overloading Comparison Operators
"""
Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.
Suppose we wanted to implement the less than symbol < symbol in our Point class.
"""
# use less than
p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1, -1)

print(p1<p2)
print(p2<p3)
print(p1 < p3)

# Similarly, the special functions that we need to implement, to overload other comparison operators are tabulated below.
"""
Operator	                Expression	    Internally
Less than	                p1 < p2	        p1.__lt__(p2)
Less than or equal to	    p1 <= p2	    p1.__le__(p2)
Equal to	                p1 == p2	    p1.__eq__(p2)
Not equal to	            p1 != p2	    p1.__ne__(p2)
Greater than	            p1 > p2	        p1.__gt__(p2)
Greater than or equal to	p1 >= p2	    p1.__ge__(p2)
"""