# -*- coding: utf-8 -*-
""""""
'''
File: 6_multiple_inheritance.py
Project: python_playground
Created Date: Tuesday-July 7-07-2020 16:23:54
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 16:23:54
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
https://www.programiz.com/python-programming/multiple-inheritance
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
"""
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
"""


class Base:
    pass


class Derived1(Base):
    pass


class Derived2(Derived1):
    pass


"""
Every class in Python is derived from the object class. It is the most base type in Python.
So technically, all other classes, either built-in or user-defined, are derived classes and all objects are instances of the object class.
"""
# Output: True
print(issubclass(list, object))

# Output: True
print(isinstance(5.5, object))

# Output: True
print(isinstance("Hello", object))

# Demonstration of MRO - Method Resolution Order in Python
"""
In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, 
left-right fashion without searching the same class twice. So, in the above example of MultiDerived class the search order is [MultiDerived, Base1, Base2, object]. 
This order is also called linearization of MultiDerived class and the set of rules used to find this order is called Method Resolution Order (MRO).
MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents. In case of multiple parents, 
the order is the same as tuples of base classes. MRO of a class can be viewed as the __mro__ attribute or the mro() method. The former returns a tuple while the latter returns a list.

Go to https: // cdn.programiz.com / sites / tutorial2program / files / MRO.jpg to see an example
"""
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())

