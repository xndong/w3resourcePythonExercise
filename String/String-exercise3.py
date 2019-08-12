# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:06:58 2019

@author: DongXiaoning
"""


def str_operation_1(astring):
    result=""
    if len(astring)<2:
        return result
    else:
        result=result+astring[:2]+astring[len(astring)-2:]
        return result

def str_operation_2(astring):
    alist=list(astring)
    if len(alist)<2:
        return ""
    else:
        result=[]
        result=alist[:2]+alist[-2:]
        return "".join(result)



input_string=input("input your string here:")
print(str_operation_1(input_string))
print(str_operation_2(input_string))

