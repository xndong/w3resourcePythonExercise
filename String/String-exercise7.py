# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:00:07 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    not_index=astring.find("not")
    poor_index=astring.find("poor")
    if not_index and poor_index:#>1 still regarded as 1 ,so true and true is true. In python ture==1, false==0
        return astring[:not_index]+'good'+astring[poor_index+len("poor"):]
    else:
        return astring

def string_operation_2(astring):
    not_index=astring.find("not")
    poor_index=astring.find("poor")
    if not_index and poor_index:
        return astring.replace(astring[not_index:poor_index+len("poor")],"good")
    else:
        return astring
    
input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))