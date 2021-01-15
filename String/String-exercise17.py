# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:03:30 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    return astring[-2:]*4

def string_operation_2(astring):
    result_alist=[]
    alist=list(astring)
    result_alist.append(alist.pop())
    result_alist.append(alist.pop())
    result_alist.reverse()
    return "".join(result_alist)*4
    #alist.pop(-2) #interesting!

input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
