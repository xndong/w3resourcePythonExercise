# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:47:50 2019

@author: DongXiaoning
"""
import math
radius = float(input("input your radius:"))
assert type(radius) == float, "Argument wrong type"
area = math.pi * radius**2
print("""The area of the circle is:""", area)

