# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 17:29:03 2023

@author: ljhdy
"""
import numpy as np

# 定义矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵加法
C = A + B
print("矩阵加法结果：")
print(C)

# 矩阵减法
C = A - B
print("矩阵减法结果：")
print(C)

# 矩阵乘法
C = np.dot(A, B)
print("矩阵乘法结果：")
print(C)

# 矩阵转置
C = A.T
print("矩阵转置结果：")
print(C)

# 矩阵求逆
C = np.linalg.inv(A)
print("矩阵求逆结果：")
print(C)

# 矩阵求行列式
C = np.linalg.det(A)
print("矩阵求行列式结果：")
print(C)
