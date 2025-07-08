# Built-in Python Modules

#   For more info, see Pyhton Standard Library

import math                     #   Built-in Standard mathematics module
import random                   #   Generates random values, e.g., integers, strings, floats, inputs, etc.
import datetime                 #   Work with, and manipulate, dat and time values.
import os                       #   Provides access to operating system dependant fxns.
import sys


#   !!  NB NB !! All modules need to be imported at the BEGINNING of the file!


'''print(math.pi)'''                  #   3.141592653589793

'''print(random.randint(0, 10))'''    #   9   ->  generates ONE number between 0 and 10.

'''print(datetime.datetime.now())'''  #   Displays the current date and time: "2025-07-08 14:48:09.565151"

'''print(os.getcwd())'''              #   Prints out the Current Working Directory of the working file: "D:\GitHub\App_Academy_GIT\python\fxn_mod_excpt"

'''print(sys.version)'''
#   Prints out the current version of Python that is running: "3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)]"