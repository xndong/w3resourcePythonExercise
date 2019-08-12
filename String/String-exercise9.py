# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:26:53 2019

@author: DongXiaoning
"""

def string_operation_1(astring,n):
    return astring[:n]+astring[n+1:]

def string_operation_2(astring,n):
    return astring.replace(astring[n],"")# the idea of ""

def string_operation_3(astring,n):
    alist=list(astring)
    alist.pop(n)
    return "".join(alist)

input_string=input("input your string here:")
index_number=int(input("input your index_n here:"))
print(string_operation_1(input_string,index_number))
print(string_operation_2(input_string,index_number))
print(string_operation_3(input_string,index_number))