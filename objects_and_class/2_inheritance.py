# -*- coding: utf-8 -*-
""""""
'''
File: inheritance.py
Project: objects_and_class
Created Date: Tuesday-July 7-07-2020 15:09:15
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:09:15
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
# parent class


class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class


class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
