# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:03:57 2019

@author: DongXiaoning
"""

def string_operation_1(astring,character):
    return astring[:astring.rfind(character)]

def string_operation_2(astring,character):
    alist=list(astring)
    while alist.pop()!=character:
        if alist==[]:
            break;
    return "".join(alist)

def string_operation_3(astring,character):
    alist=astring.rsplit(character,1) #nice!
    return alist[0]

input_string_1=input("input your string here:")
input_string_2=input("input your string here:")
print(string_operation_1(input_string_1,input_string_2))
print(string_operation_2(input_string_1,input_string_2))
print(string_operation_3(input_string_1,input_string_2))

