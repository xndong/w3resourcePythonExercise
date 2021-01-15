# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:07:35 2019

@author: DongXiaoning
"""

def string_operation_1(str1,str2):
    x=str1[:2]
    y=str2[:2]
    result=''''''
    tmp=''
    for char1 in str1:
        result+=char1
    result=y+result[2:]+' '
    for char2 in str2:
        tmp+=char2
    tmp=x+tmp[2:]
    result+=tmp
    return result

def string_operation_2(str1,str2):
    new_str1=str1[:2]+str2[2:]
    new_str2=str2[:2]+str1[2:]
    return new_str2+' '+new_str1

input_string_1=input("input your string1 here:")
input_string_2=input("input your string2 here:")
print(string_operation_1(input_string_1,input_string_2))
print(string_operation_2(input_string_1,input_string_2))