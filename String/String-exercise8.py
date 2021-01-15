# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:05:06 2019

@author: DongXiaoning
"""

def string_operation_1(astring):
    #result_tuple=()
    maxlen=0
    alist=astring.split(' ')
    for list_element in alist:
        if len(list_element)>maxlen:
            maxlen=len(list_element)
            result_list=[list_element,maxlen]
        elif len(list_element)==maxlen: #最长的可能多个，i.e.它们相等
            result_list+=[list_element,maxlen]
        else:
            pass
    result_tuple=tuple(result_list)
    return result_tuple

def string_operation_2(astring):
    maxlen=0
    result_dictionary={}
    alist=astring.split(' ')
    for list_element in alist:
        if len(list_element)>maxlen:
            maxlen=len(list_element)
            result_dictionary.clear() #result_dictionary={} 差别在于前者不重开内存，起始地址不变。
            result_dictionary[list_element]=len(list_element)
        elif len(list_element)==maxlen: #最长的可能多个，i.e.它们相等
            result_dictionary[list_element]=len(list_element)
        else:
            pass
    return result_dictionary

#Top-k 优先级队列
#元素去重 set有没有直接的方法？
#数字的大小顺序就是一种优先级，you can define the prioty with your own rules
#another idea:前5名，就是将优先级队列pop(0) 5次(if没有重复元素)
    

def string_operation_3(astring):
    maxlen=0
    result_dictionary={}
    alist=astring.split(' ')
    for list_element in alist:
        if len(list_element)>maxlen:
            maxlen=len(list_element)
            result_dictionary.clear() #result_dictionary={} 差别在于前者不重开内存，起始地址不变。
            result_dictionary[list_element]=len(list_element)
        elif len(list_element)==maxlen: #最长的可能多个，i.e.它们相等
            result_dictionary.update({list_element:maxlen}) #obviously can not "+" because of key is unique
        else:
            pass
    return result_dictionary


def string_operation_4(astring):
    maxlen=0
    result_dictionary={}
    alist=astring.split(' ')
    for list_element in alist:
        if len(list_element)>maxlen:
            maxlen=len(list_element)
            result_dictionary.clear()               
        elif len(list_element)<maxlen:
            continue
        else:
            pass
        result_dictionary.update({list_element:maxlen})
    return result_dictionary


input_string=input("input your string here:")
print(string_operation_1(input_string))
print(string_operation_2(input_string))
print(string_operation_3(input_string))
print(string_operation_4(input_string))

#max(),min(),sort()在有多个相等的最值的时候，就不如我自己的方法好。所以，下面的solution是有缺陷的。
def find_longest_word(words_list):
    '''w3resource's solution'''
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()        #let's talk about sort()
    return word_len[-1][1] #perfect!word_len is not a two-dimension matrix. Instead, it is a nested structure of list and tuple 

print(find_longest_word(["PHP", "Exercises", "Backend"]))