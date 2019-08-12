# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:51:42 2019

@author: DongXiaoning
"""

#格式化字符串 %-2.3f   %varible or tuple or object。会把它们变成格式化(有组织、有纪律)的字符串类型
#also like a placeholder
#显然格式化字符串要么出现在其他字符串内部，要不单独存在

def add_tags_1(tag,string):
    left_tag_list=['<',tag,'>']
    right_tag_list=['</',tag,'>']
    return "".join(left_tag_list)+string+"".join(right_tag_list)

def add_tags_2(tag,string):
    tag_list=['<',tag,'>','</',tag,'>']
    tag_list.insert(3,string)
    return "".join(tag_list)

#格式化输入输出
def add_tags_3(tag,string):
    tag1='<'+tag+'>'
    tag2='</'+tag+'>'
    return tag1,string,tag2

def add_tags_4(tag,string):
    return "<%s>%s</%s>" %(tag,string,tag)

def add_tags_5(tag,string):
    atuple=(tag,string,tag)
    return "<%s>%s</%s>" %atuple

tag=input("input your tag here:")
string=input("input your string here:")
print(add_tags_1(tag,string))
print(add_tags_2(tag,string))
print("%s%s%s" %(add_tags_3(tag,string)))
print(add_tags_4(tag,string))
print(add_tags_5(tag,string))


#You designed the function, so when writting the function code, you know the type of the function parameter(i.e. varible)
#But for those who call or invoke the function, how do they know what type of varible can be input into the fuction?
#That's how docstring works, i.e. you ought to write docstring to achieve abstraction(MIT Open Courese):
#function:This function is defined to ...
#input: tag is string type and ....; string is string type and ...
#output: This function output a tuple, and they are....
