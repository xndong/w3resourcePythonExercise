# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:03:07 2019

@author: DongXiaoning
"""

def string_operation_1(astring_1,astring_2):
    alist_1=list(astring_1)
    alist_2=list(astring_2)
    alist_1.insert(len(astring_1)//2,alist_2) #wrong solution
    print(alist_1) #print it out, then you will find what is wrong
    return None

def string_operation_2(astring_1,astring_2):
    assert len(astring_1)%2==0, "the length of the first parameter must be odd"
    alist_1=list(astring_1)
    alist_tmp=[]
    while len(alist_1)!=len(alist_tmp):
        alist_tmp.append(alist_1.pop(0))
    return "".join(alist_tmp)+astring_2+"".join(alist_1)

def string_operation_3(astring_1,astring_2):
    assert len(astring_1)%2==0, "the length of the first parameter must be odd"
    return astring_1[:len(astring_1)//2]+astring_2+astring_1[len(astring_1)//2:]

def string_operation_4(astring_1,astring_2):
    atuple=(astring_1[:len(astring_1)//2],astring_2,astring_1[len(astring_1)//2:])
    return "%s%s%s"%atuple

input_string_1=input("input your string here:")
input_string_2=input("input your string here:")

print(string_operation_2(input_string_1,input_string_2))
print(string_operation_3(input_string_1,input_string_2))
print(string_operation_3(input_string_1,input_string_2))
    