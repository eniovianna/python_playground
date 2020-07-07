# -*- coding: utf-8 -*-
""""""
'''
File: polymorphism.py
Project: objects_and_class
Created Date: Tuesday-July 7-07-2020 15:13:04
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:13:4
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
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)


"""
Key Points to Remember:
Object-Oriented Programming makes the program easy to understand as well as efficient.
Since the class is sharable, the code can be reused.
Data is safe and secure with data abstraction.
Polymorphism allows the same interface for different objects, so programmers can write efficient code.
"""