# -*- coding: utf-8 -*-
""""""
'''
File: urllib_.py
Project: advanced
Created Date: Tuesday-July 7-07-2020 14:38:34
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-July 7-07-2020 14:38:34
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc

-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
# urllib contains 05 modules:
# request => open URLs
# response => (used internally)
# error => request exceptions
# parse => useful URL functions
# robotparser => robots.txt files

"""
import urllib 
print(dir(urllib))
print(help(urllib))
"""
from urllib import parse
from urllib import request
print(dir(request))
print(help(request))

resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))
print(dir(resp))
print(help(resp))
print(resp.code)  # 200 (ok); 400 (bad request); 403 (forbidden); 4004 (not found)
print(resp.peek())  # The letter 'b' in the beginning represent a bytes object
data = resp.read()
html = data.decode("UTF-8")
print(type(html))

# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s
print(dir(parse))
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://youtube.com" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")