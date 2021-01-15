# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:03:45 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    if len(astring)<3:
        return astring
    else:
        return astring[:3]
    
input_string=input("input your string here:")
print(string_operation_1(input_string))