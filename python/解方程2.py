# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:38:24 2023

@author: ljhdy
"""

from sympy import *
from sympy.abc import x, y, a, b

# Define the equations
eq1 = Eq(y, 2*x + 1)
eq2 = Eq(x**2/a**2 + y**2/b**2, 1)

# Solve for the intersection points
sol = solve((eq1, eq2), (x, y))

# Print the coordinates of the intersection points
for point in sol:
    print(f"({point[0]}, {point[1]})")

# Print the condition of the equation
print(f"The condition of the equation is a^2 > 0 and b^2 > 0.")

# Output the coordinates of the intersection points in LaTeX format
for point in sol:
    print(f"\\left({latex(point[0])}, {latex(point[1])}\\right)")