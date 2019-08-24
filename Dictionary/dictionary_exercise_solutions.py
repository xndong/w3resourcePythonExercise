# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:44:38 2019

@author: Dong Xiaoning
"""

import itertools
import operator

def sort_by_value(dictionary):
    result_list = sorted(dictionary.items(),key = operator.itemgetter(1))
    #dictionary.items()返回一个list,element是一个个的(key,value) binary tuple
    #sorted()的返回值是list,element也就是dictionary.items()的element(i.e. binary tuple)
    result_dictionary = dict(result_list)
    print(result_list)
    print(result_dictionary)
    return result_dictionary

def concatenate_dictionary(dic_one,dic_two):
    iter_one = dic_one.items()
    iter_two = dic_two.items()
    dic_iter = itertools.chain(iter_one,iter_two)
    # dic_iter is an iterable object
    # dict()不会造成重复元素,字典key是unique的,dict()过程中，如果出现重复的key,后面会覆盖前面的。
    result = dict(dic_iter)
    print(result)
    return result

# idea: continuously update a dictionary
def concatenate_dictionary_2(dic_one,dic_two):
    generator_object = (dic_one,dic_two) # tuple
    result = {}
    for d in generator_object:
        result.update(d)
    print(result)
    return result

def is_key_exist(key, dictionary):
    return (False,True)[key in dictionary]

def traverse_dictionary(dictionary):
    for key in dictionary:
        print('key: ',key,' -> value: ',dictionary[key])
    return
def traverse_dictionary_2(dictionary):
    for key,value in dictionary.items(): #返回一个list,element是一个个的binary tuple。是tuple就可以x, y = (e1,e2)
        print('key: ',key,' -> value: ',value)

def create_dictionary(n):
    result_dictionary = {}
    for i in range(1,n):
        result_dictionary[i] = i**2
    return result_dictionary

def create_dictionary_2(n):
    list_comprehension = [(i,i**2) for i in range(1,n)]
    return dict(list_comprehension)

def create_dictionary_3(n):
    list_comp_one = [i for i in range(1,n)]
    list_comp_two = [i**2 for i in list_comp_one]
    list_comprehension = [(x,y) for x in list_comp_one for y in list_comp_two] # 这不是在做zip()操作么.     #字符串的话str(x) + str(y)  or '{}{}'.format(x,y)
    # wrong, it will not executed like zip(),而是会产生笛卡尔乘积. Algouth you want to do zip() in your mind,
    # the wrong code will not perform as what you thought in your mind.
    result_dictionary = dict(list_comprehension)
    return result_dictionary

# zip() zip two lists into one list, where its element is a binary tuple.
# eg [1,2,3]
#    ['a','b','c']
#    [(1,'a'),(2,'b'),(3,'c')]

# solution 4,5,6 --> map two lists into a dictionary
def create_dictionary_4(n):
    list_comp_one = [i for i in range(1,n)]
    list_comp_two = [i**2 for i in list_comp_one]
    result_dictionary = dict(zip(list_comp_one,list_comp_two))                 #直接用zip()函数
    return result_dictionary

def create_dictionary_5(n):
    result_dictionary = {}
    list_comp_one = [i for i in range(1,n)]
    list_comp_two = [i**2 for i in list_comp_one]
    for x,y in zip(list_comp_one,list_comp_two):
        result_dictionary[x] = y
    return result_dictionary

def create_dictionary_6(n): # dictionary comprehension
    list_comp_one = [i for i in range(1,n)]
    list_comp_two = [i**2 for i in list_comp_one]
    return {x:y for x,y in zip(list_comp_one,list_comp_two)}

# map(func,iterable) and list comprenhension and dictionary comprenhension
# can we pass a function to list comprehension's first parameter? just as in map()'s first parameter.
# The answer is yes. Thus, both function or expression is applicable for the first parameter! see the following example:
def power2(x):
    return x**2
def list_comprehense():
    list_comprehension = [power2(x) for x in range(5,11)]
    print(list_comprehension)

def merge_dictionary(dict_one,dict_two): # concatenate, merge --> update()
    dict_one.update(dict_two) #update() return a bool value! but dict_one has been modified.
    return dict_one

def delete_dictionary_item(dictionary,key):
    if key in dictionary:
        del dictionary[key]
    else:
        print("key does not exist.")
    return dictionary

def sort_by_key(dictionary):
    return dictionary

def main():
    dic={'X':5,'B':4,'Y':3,'D':2,'E':1}
    sort_by_value(dic)
    dic_one = dic
    dic_two = {'P':10,'Q':100}
    concatenate_dictionary(dic_one,dic_two)
    concatenate_dictionary_2(dic_one,dic_two)
    print(is_key_exist('X',dic))
    traverse_dictionary(dic_two)
    traverse_dictionary_2(dic_two)
    print(create_dictionary(5))
    print(create_dictionary_2(5))
    print(create_dictionary_3(5))
    print(create_dictionary_4(5))
    print(create_dictionary_5(5))
    print(create_dictionary_6(5))
    list_comprehense()
    print(merge_dictionary(dic_one,dic_two))






    return

if __name__ == '__main__':
    main()
