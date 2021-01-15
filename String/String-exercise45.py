# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:15:46 2019

@author: DongXiaoning
"""

import string

def string_operation_1(astring):
    astring=astring.lower()
    a_dictionary={}.fromkeys(string.ascii_lowercase)
    for dictionary_element in a_dictionary:
        a_dictionary[dictionary_element]=False
    for character in astring:
        if character in string.ascii_lowercase:
            a_dictionary[character]=True
        else:
            pass
    result=True
    for flag in a_dictionary.values():
        result=flag and result
    return result

def string_operation_2(astring):
    astring=astring.lower()
    result_dictionary={}
    for character in astring:
        if character in string.ascii_lowercase:
            result_dictionary[character]=True
        else:
            pass
    if len(result_dictionary)==26:
        return True
    else:
        return False
    
def string_operation_3(astring):
    astring=astring.lower()
    result_list=[]
    for character in astring:
        if character in string.ascii_lowercase:
            result_list.append(character)
        else:
            pass
        result_list=list(set(result_list))#去重
    if len(result_list)==26: 
    #if result_list==list(string.ascii_lowercase):
    #if "".join(result_list)==string.ascii_lowercase:
        return True
    else:
        return False
    
def string_operation_4(astring):
    astring=astring.lower()
    target_set=set(string.ascii_lowercase)
    result_list=[]
    for character in astring:
        if character in string.ascii_lowercase:
            result_list.append(character)
        else:
            pass
    result_set=set(result_list)
    if target_set.intersection(result_set)!=target_set:
        return False
    else:
        return True
    
def string_operation_5(astring):
    astring=astring.lower()
    target_set=set(string.ascii_lowercase)
    if target_set.intersection(set(astring))==target_set:
        return True
    else:
        return False
    
    

input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
print(string_operation_3(input_string))
print(string_operation_4(input_string))
print(string_operation_5(input_string))
    