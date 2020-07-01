# -*- coding: utf-8 -*-
""""""
'''
File: logging_.py
Project: intermediate
Created Date: Tuesday-June 30-06-2020 21:48:44
Author: Ênio Rodrigues Viana
-----
Last Modified: Tuesday-June 30-06-2020 21:48:44
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

# Purpose: Record progress and problems...
# Levels: Debug, Info, Warning, Error, Critical
import math
import logging
print(dir(logging))

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="lumberjack.log",
                    level=logging.DEBUG, format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()

# Test the logger
logger.info("Our first message.")
# Nothing will be written
# 30 because it is default, to change it we need to change our logging level
print(logger.level)
# There are 6 built-in level constants
# Level     -   Numeric Value
# NOT SET   -   0
# DEBUG     -   10
# INFO      -   20
# WARNING   -   30
# ERROR     -   40
# CRITICAL  -   50

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire internet is down!!")

# A mathematical example


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)
    
    # Return the roots
    logger.debug("# Return the roots")
    return(root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)
roots = quadratic_formula(1, 0, 1)
print(roots)