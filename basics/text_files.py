# -*- coding: utf-8 -*-
""""""

'''
File: text_files.py
Project: basics
Created Date: Wednesday-July 1-07-2020 23:31:05
Author: Ênio Rodrigues Viana
Based on Youtube channel Socratica
-----
Last Modified: Wednesday-July 1-07-2020 23:31:5
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
with open("guido_bio.txt") as f:
    text = f.read()
# The code below is more security than above. When we uses open method
# we don't need to close the file.
with open("guido_bio.txt") as fobj:
    bio = fobj.read()
print(bio)

# If we try to open a file that don't exist we will receive a error.
# with open("guido_bio_utopic.txt") as fobj:
#     bio_utopic = fobj.read()
# print(bio_utopic)
# The simple way to avoid this is using a try except
try:
    with open("guido_bio_utopic.txt") as f:
        text = f.read()
except FileNotFoundError as err:
    text = None
    # print(err.strerror)
finally:
    print(text)

# The code below show us how to create and populate a file.
# By default *open* uses read mode. So, if we need to write a file we need to open
# it in write(w) mode.
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean + "\n")
# There is another way to write in a file, in that we use print. 
# This method cause the same effect, but we didn't need to write breaklines.
with open("oceans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

# If necessary we can open a file to add more contents preserving the old contents,
# for this we need to open a file in append mode.
with open("oceans.txt", "a") as f:
    print(23*"="+ "\nThere are 5 oceans.", file=f)