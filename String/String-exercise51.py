# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:51:38 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    for character in astring:
        left_most_index=astring.find(character)
        if astring.find(character,left_most_index+1)==-1:
            return character
    return None

def string_operation_2(astring):
    for character in astring:
        if astring.find(character)==astring.rfind(character): #Note that always return 正序的index, no matter rfind() or find(),其余返回索引的函数也是如此，并不是说rfind()返回的索引就是r——从右往左的负值。
            return character
    return None

input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
