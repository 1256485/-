# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:26:22 2023

@author: ljhdy
"""

def hanoi(n, A, B, C):
    if n == 1:
        print(A, '-->', C)
        return 1
    else:
        hanoi(n-1, A, C, B)
        count = hanoi(n-1, A, C, B)
        print(A, '-->', C)
        hanoi(n-1, B, A, C)
        count += hanoi(n-1, B, A, C)
        return count

hanoi(10, 'A', 'B', 'C')
count = hanoi(10, 'A', 'B', 'C')
print("移动次数：", count)
