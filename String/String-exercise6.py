# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:43:36 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    if len(astring)<3:
        return astring
    elif astring[-3:]=="ing":
        return astring[:]+"ly"
    else:
        return astring+"ing"
#自己重新梳理整理了branching的逻辑顺序，not just follow the order of what the exercise said and then write code.
def string_operation_2(astring):
    if len(astring)<3:
        return astring
    elif astring.endswith("ing"):
        return astring+"ly"
    else:
        return astring+"ing"

def string_operation_3(astring):
    '''This is the w3resouce's solution'''
    if len(astring)>2:
        if astring[-3:]=="ing":
            astring+='ly'
        else:
            astring+="""ing"""
    else:
        pass
    return astring


input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))