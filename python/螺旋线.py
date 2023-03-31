# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:56:28 2023

@author: ljhdy
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

ax.plot3D(x, y, z, 'red')
ax.set_title('3D line plot')
plt.show()

