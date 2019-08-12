# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:31:56 2019

@author: DongXiaoning
"""

def reverse_string_1(astring):
    if not len(astring)%4:
        alist=list(astring)
        alist.reverse()
        return "".join(alist)
    else:
        return astring

def reverse_string_2(astring):
    if not len(astring)%4:
        return astring[::-1]
    else:
        return astring
def reverse_string_3(astring):
    if not len(astring)%4:
        alist=list(astring)
        result_alist=[]
        while alist!=[]:
            result_alist.append(alist.pop())
        return "".join(result_alist)
    else:
        return astring
    
input_string=input("input your string here:")
print(reverse_string_1(input_string))
print(reverse_string_2(input_string))
print(reverse_string_3(input_string))

