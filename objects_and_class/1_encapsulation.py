# -*- coding: utf-8 -*-
""""""
'''
File: encapsulation.py
Project: python_playground
Created Date: Tuesday-July 7-07-2020 15:10:35
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 15:10:35
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


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
