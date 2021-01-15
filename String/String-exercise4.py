# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:36:17 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    alist=astring.split(astring[0])
    str_tmp="$".join(alist)
    str_result=astring[0]+str_tmp[1:]
    return str_result


def string_operation_2(astring):
    alist=list(astring)
    target=alist[0]
    result=[]
    while alist!=[]:
        pop_element=alist.pop(0)
        if pop_element==target:
            result.append('$')
        else:
            result.append(pop_element)
    result[0]=target
    return "".join(result)


def string_operation_3(astring):
    alist=list(astring)
    target=alist[0]
    result=""
    while alist!=[]:
        pop_element=alist.pop(0)
        if pop_element==target:
            result+="$"
        else:
            result+=pop_element
    return target+result[1:] 


def string_operation_4(astring):
    target=astring[0]
    result=""
    for char in astring:
        if char==target:
            result+='$'
        else:
            result+=char
    return target+result[1:]

def string_operation_5(astring):
    target=astring[0]
    result=astring.replace(target,'$')
    return target+result[1:]        


input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
print(string_operation_3(input_string))
print(string_operation_4(input_string))
print(string_operation_5(input_string))