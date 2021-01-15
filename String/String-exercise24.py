# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:23:30 2019

@author: DongXiaoning
"""

def string_operation_1(astring,character):
    assert isinstance(astring,str),"The first function parameter must be string type"
    return astring.startswith(character)

input_string=input("input your string here:")
input_character=input("input your character here:")
print(string_operation_1(input_string,input_character))

