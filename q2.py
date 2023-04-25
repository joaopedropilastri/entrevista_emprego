# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:10:42 2023

@author: jterr
"""

n = int(input())

a, b = 0, 1

while a < n:
    a, b = b, a + b

print(a == n)