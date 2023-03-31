# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:52:57 2023

@author: ljhdy
"""
import sympy as sp
from sympy.abc import x
y = sp.Function('y')(x)
eq = sp.Eq(y.diff(x, 3) + 2*y.diff(x, 2) - y.diff(x) - 2*y, sp.exp(x))
sol = sp.dsolve(eq)
print(sol)