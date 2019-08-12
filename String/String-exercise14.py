# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:03:24 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    alist=astring.split(',')
    #unique
    result_alist=[]
    for list_element in alist:
        if list_element not in result_alist:
            result_alist.append(list_element)
    print(result_alist)
    result_alist.sort()
    return ",".join(result_alist)

input_string=input("input your string here:")
print(string_operation_1(input_string))




'''
while dealing with 元素去重，尽管上述方法行之有效，但我们在exercise就有过思考，
能不能利用Set具有unique的性质或者Dictionary的key具有unique的性质来快速去重,It turns out your 猜想 is truely right!
'''

def list_unique_1(alist):
    return list(set(alist))

def list_unique(alist):
    return list({}.fromkeys(alist).keys())


    