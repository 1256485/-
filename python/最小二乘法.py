# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:25:47 2023

@author: ljhdy
"""
import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 1.9, 3.2, 4.1, 5.3])

# Fit a line to the data using least squares
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Plot the data and the fitted line
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()