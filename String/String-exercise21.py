# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:54:09 2019

@author: DongXiaoning
"""
import string
def string_operation_1(astring):
    capital_letters=string.ascii_uppercase
    test_set=set(astring[:4])
    result_set=test_set.intersection(set(capital_letters))
    if len(result_set)>=2:
        return astring.upper()
    else:
        return astring
    
def string_operation_2(astring):
    capital_letter_count=0
    for index,character in enumerate(astring):
        if index<4:
            if character in string.ascii_uppercase:
                capital_letter_count+=1
            else:
                pass
        else:
            break
    if capital_letter_count>=2:
        return astring.upper()
    else:
        return astring


def string_operation_2_5(astring):
    capital_letter_count=0
    for index,character in enumerate(astring[:4]): #nice! iterate astring[:4] not the whole astring
        if character in string.ascii_uppercase:
            capital_letter_count+=1
        else:
            pass
    if capital_letter_count>=2:
        return astring.upper()
    else:
        return astring


    
def string_operation_3(astring):
    capital_letter_count=0
    alist=list(astring)
    for i in range(4):
        if alist.pop(0) in string.ascii_uppercase:
            capital_letter_count+=1
        else:
            pass
    if capital_letter_count>=2:
        return astring.upper()
    else:
        return astring
    
def string_operation_4(astring):
    capital_letter_count=0
    for char in astring[:4]:
        if char in string.ascii_uppercase:
            capital_letter_count+=1
        else:
            pass
    if capital_letter_count>=2:
        return astring.upper()
    else:
        return astring
    
    
input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
print(string_operation_2_5(input_string))
print(string_operation_3(input_string))
print(string_operation_4(input_string))
        