"""! @brief Problem: To have an initial Python script to play with"""
## @file PythonApplication1.py
# @unclassified
# @library(python_applications)
# @author Kem White
# @date 15 June 2021
# @brief This is a simple Python program to help me learn Python
# Target Users: Me
# @copyright Copyright (C), 2020 Johns Hopkins University/Applied Physics Laboratory.
# Permission to copy all or part of this work is granted, provided that
# the copies are made or distributed only for the Virtual Ownship project and that
# this copyright notice remains intact. For any other permissions please
# contact the Johns Hopkins University Applied Physics Laboratory.
# Target System: Windows
# Interface: Command Line
# Functional Requirements: TBD. For now just do some simple stuff
# Testing: 
# Maintainer: Kem White

import numpy as np
import sys
import pickle
print("Hello, world?")
##
# Create 2 new lists height and weight
print("Hello, world!")
print("Hello, hello!, HELLO! world!")
#%%
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
print(height)
print(weight)

#%%

print(height)
print(weight)

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

myPi = np.pi	
myNum = myPi*100
print("myPi= ", myPi)
print("myNum= ", myNum)

hooBoy = np.array([[6., 5., 4.], [3., 2., 1.]])
print(hooBoy[0,0])
print(hooBoy[0,1])
print(hooBoy[0,2])
print(hooBoy[1,0])
print(hooBoy[1,1])
print(hooBoy[1,2])
print(hooBoy)
