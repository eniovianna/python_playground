# -*- coding: utf-8 -*-
""""""
'''
File: basics.py
Project: objects_and_class
Created Date: Tuesday-July 7-07-2020 15:00:46
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:00:46
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

    # class attribute
    species = "bird"

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


def main():
    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    # access the class attributes
    print("Blu is a {}".format(blu.__class__.species))
    print("Woo is also a {}".format(woo.__class__.species))

    # access the instance attributes
    print("{} is {} years old".format(blu.name, blu.age))
    print("{} is {} years old".format(woo.name, woo.age))

    # call our instance methods
    print(blu.sing("'Happy'"))
    print(blu.dance())


if __name__ == "__main__":
    main()
