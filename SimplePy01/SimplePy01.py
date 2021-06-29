# Problem: To have an initial Python script to play with
# Target Users: Me
# Target System: Windows
# Interface: Command Line
# Functional Requirements: TBD. For now just do some simple stuff
# Testing: 
# Maintainer: Kem White

import numpy as np
import random
print("Hello, world?")

# Create 2 new lists height and weight
print("Hello, world!")
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

print(np.pi)

myVar = random.gauss(0,1)
print(myVar)
print(random.gauss(0,1))