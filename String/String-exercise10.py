# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:38:02 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    return astring[-1]+astring[1:-1]+astring[0]  #astring[1:len(astring)-2] is ugly, every element has an ordered index and a reverse-order index

  
input_string=input("input your string here:")
print(string_operation_1(input_string))


