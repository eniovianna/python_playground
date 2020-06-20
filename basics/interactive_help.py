'''
Filename: c:\python_playground\basics\interactive_help.py
Path: c:\python_playground\basics
Created Date: Saturday, June 20th 2020, 7:00:22 pm
Author: Ênio Viana

Copyright (c) 2020 eniocc
Based on Socratica videos
'''

print(dir())
print(80*"=")

print(dir(__annotations__))
print(80*"=")

print(dir(__builtins__))
print(80*"=")

print(help(pow))
print(80*"=")

#print(help('modules'))

# The code line below will generate an error
# print(dir(math))
# To run it correctly we need import the correct module
import math
print(dir(math))

# Now, let's try to print help for 'log'
# print(help(log))
# The code above has an error because we need use the full path, see below
print(help(math.log))