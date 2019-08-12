# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:06:46 2019

@author: DongXiaoning
"""

str_counted=input('''Input the string:''')
dic_count={}
for char in str_counted:
    if char not in dic_count.keys():
        dic_count[char]=1
    elif char in dic_count:
        dic_count[char]+=1
    else:
        pass
print(dic_count)