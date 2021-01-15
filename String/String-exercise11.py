# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:56:21 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    alist=list(astring)
    flag=True
    result_list=[]
    while alist!=[]:
        if flag:
            result_list.append(alist.pop(0))
            flag=False
        else:
            alist.pop(0)
            flag=True
    return "".join(result_list)

def string_operation_2(astring):
    flag=True
    for character in astring:
        if flag:
            flag=False
        else:
            astring=astring.replace(character,"") ####Wrong solution, because replace() method will replace all matched character
            flag=True
    return astring

def string_operation_3(astring):
    result_string=""
    flag=False
    for character in astring:
        if flag:
            flag=False
        else:
            result_string+=character
            flag=True
    return result_string

def string_operation_4(astring):
    result_string=""
    for i in range(len(astring)):
        if i%2==0:
            result_string+=astring[i]
        else:
            pass
    return result_string

def string_operation_5(astring):
    result_string=""
    for index,character in enumerate(astring):
        if index%2==0:
            result_string+=character
        else:
            pass
    return result_string


#hard_match 某一集合内描述的element
def string_operation_6(astring):
    result_string=""
    hard_match=(1,2,4,9) #硬匹配 List [1,2,4,9] or String "1249" or Set {1,2,4,9} make no difference
    for index,character in enumerate(astring): #enumerate() is incredibly friendly to our sequence who is indexed by an integer.
        if index in hard_match: #if index in (1,2,4,9)
            result_string+=character
        else:
            pass
    return result_string

    
            

input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
print(string_operation_3(input_string))
print(string_operation_4(input_string))
print(string_operation_5(input_string))

#hard_match 某一集合内描述的element
print(string_operation_6(input_string))





