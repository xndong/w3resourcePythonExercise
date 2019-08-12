# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:37:26 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    return astring.upper(),astring.lower(),astring.capitalize(),astring.title(),astring.swapcase()


input_string=input("input your string here:")
upper,lower,cap,title,swapcase=string_operation_1(input_string)
print(upper)
print(lower)
print(cap)
print(title)
print(swapcase)


#upper() lower() title() captialize()