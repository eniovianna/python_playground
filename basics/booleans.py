'''
Filename: c:\python_playground\basics\booleans.py
Path: c:\python_playground\basics
Created Date: Saturday, June 20th 2020, 7:08:48 pm
Author: Ênio Viana

Copyright (c) 2020 eniocc
Based on Socratica videos
'''

# Boolean values: True, False
print(True)
print(False)
# Be careful, case sensitive alert!
#print(true)
#print(false)

a = 3
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)

print(type(True))
print(type(False))

# In Python every number different 0 converted in Boolean is 1
print(bool(28))
print(bool(-2.71828))
print(bool(0))

# It is possible convert Strings to boolean
print(type('True'))     # It is a string
print(type('False'))    # It is a string
print(bool('True'))     # It is a string
print(bool('False'))    # It is a boolean
print(bool('Turing'))   # It is a boolean
print(bool(' '))        # It is a boolean

# In Python only empty string is False, all the others is true
print(bool(''))         # It is a boolean

# Boolean conversions rule
#trivial values        => False
#non-trivial values    => True

# It's also possible convert boolean to another types
str(True)       # It is a string
str(False)      # It is a string
int(True)       # It is a integer
int(False)      # It is a integer

# It is also possible use arithmetics operatos with boolean and others types
print(5 + True)     # 1 is equal True, and vice-versa
print(10 * False)   # 0 is equal False, and vice-versa