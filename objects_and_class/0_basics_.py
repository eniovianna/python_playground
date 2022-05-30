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
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"


def main():
    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    # access the class attributes
    print(f"Blu is a {blu.__class__.species}")
    print(f"Woo is also a {woo.__class__.species}")

    # access the instance attributes
    print(f"{blu.name} is {blu.age} years old")
    print(f"{woo.name} is {woo.age} years old")

    # call our instance methods
    print(blu.sing("'Happy'"))
    print(blu.dance())


if __name__ == "__main__":
    main()
