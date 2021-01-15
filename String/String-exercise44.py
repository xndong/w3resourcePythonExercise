# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:00:31 2019

@author: DongXiaoning
"""


def character_index(astring):
    for index,character in enumerate(astring): #index,character is a tuple(i.e. (index,character))
        #enumerate()返回一个元素为tuple(index,character)的list. 
        #Note that a,b (a,b) make no difference,they are tuple type.
        #You can type a=2 b=3 a,b or type 2,3 directly on Python Console(交互式解释器), then you will find both of them are tuple type
        print("Current character %s position at %d"%(character,index))
    return None
    
input_string=input("input your string here:")
character_index(input_string)