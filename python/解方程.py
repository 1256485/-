# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:32:33 2023

@author: ljhdy
"""

from sympy import symbols, solve, latex

# Define variables
x, y, k, b, m, n = symbols('x y k b m n')

# Define equations
eq1 = y - k*x - b
eq2 = x**2/m**2 + y**2/n**2 - 1

# Solve for intersection points
sol = solve((eq1, eq2), (x, y))

# Print results
print(latex(sol))
