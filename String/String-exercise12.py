# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:37:24 2019

@author: DongXiaoning
"""

#analysis
#omit the punctuation;words are separted by space

import string

#delete all punctuations except '(' in a sentence(i.e. astring) then use space to replae '('
def string_preprocess_1(astring):
    hard_match=string.punctuation
    hard_match=hard_match.replace('(',"") #a careful way to remove an element from a string, because replace means all will be replaced 
    result_tmp=astring
    for punctuation in hard_match:
        if punctuation in astring:
            result_tmp=result_tmp.replace(punctuation,"")
        else:
            pass
    #单独处理'('
    if '(' in result_tmp:
        result_tmp=result_tmp.replace('('," ")
    return result_tmp
    

#delete all punctuations except '(' in a sentence(i.e. astring) then use space to replae '('
def string_preprocess_2(astring):
    hard_match=string.punctuation
    result_tmp=astring
    for punctuation in hard_match:
        if punctuation in astring and punctuation!='(':
            result_tmp=result_tmp.replace(punctuation,"")
        elif punctuation in astring and punctuation=='(':
            result_tmp=result_tmp.replace(punctuation," ")
        else:
            pass
    return result_tmp

 #yet another loop
def string_preprocess_3(astring):
    hard_match=string.punctuation
    result_tmp=""
    for character in astring:
        if character in hard_match and character!='(':
            pass
        elif character in hard_match and character=='(':
            result_tmp+=' '
        else:
            result_tmp+=character
    return result_tmp

def string_preprocess_4(astring):
    hard_match=string.punctuation
    result_tmp=""
    for character in astring:
        if character not in hard_match:
            result_tmp+=character
        elif character in hard_match and character=='(':
            result_tmp+=' '
    return result_tmp





#count the occurrence of a word in a sentence
#Be careful of such case: I love China(i.e. People's Republic of China)
def string_operation_1(astring):
    result={}    #list,dictionary and tuple make difference in this case while make no difference in exercise8
    astring=string_preprocess_2(astring)
    alist=astring.split(' ')
    for list_element in alist:
        if list_element not in result:
            result[list_element]=1
        elif list_element in result:
            result[list_element]+=1
        else:
            pass
    return result

input_string=input("input your string here:")

print(string_preprocess_1(input_string))
print(string_preprocess_2(input_string))
print(string_preprocess_3(input_string))
print(string_preprocess_4(input_string))

print(string_operation_1(input_string))




    
    
    
    

    
    

        
        
        
        




        
    
    
    
    