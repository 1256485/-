# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:23:37 2023

@author: ljhdy
"""

# 导入必要的库
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义常微分方程组
def model(y, t):
    dydt = np.zeros(2)
    dydt[0] = -y[0] + y[1]
    dydt[1] = y[0] - y[1]
    return dydt

# 定义初始条件
y0 = [1, 0]

# 定义时间点
t = np.linspace(0, 10, 101)

# 解常微分方程组
y = odeint(model, y0, t)

# 绘制结果
plt.plot(t, y[:, 0], 'r-', label='y1(t)')
plt.plot(t, y[:, 1], 'b--', label='y2(t)')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
