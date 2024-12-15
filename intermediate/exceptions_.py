# -*- coding: utf-8 -*-
""""""
'''
File: exceptions.py
Project: intermediate
Created Date: Tuesday-June 30-06-2020 18:14:32
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-June 30-06-2020 18:14:32
Modified By: the developer formerly known as Ênio Rodrigues Viana at <eniocc@gmail.com>
-----
Copyright (c) 2020 eniocc
Based on Youtube channel Socratica
-----
HISTORY:
Date      	By	Comments
----------	---	---------------------------------------------------------
'''
""""""
 # Common structure of an exception
 # try:
    # Runs first
    # <code>
 # except:
    # Runs if exception occurs in try block
    # <code>
 # else:
    # Executes if try block *succeeds*
    # <code>
 # finally:
    #  This code *always* executes
    # <code>

import logging
import time

# Create logger
logging.basicConfig(filename = "C:\\python_playground\\intermediate\\problems.log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        return f.read()
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

data = read_file_timed("F:\\3_ambos\\musicas\\80's\\01\\Camila Camila.mp3")