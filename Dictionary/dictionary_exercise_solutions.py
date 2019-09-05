# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:44:38 2019

@author: Dong Xiaoning
"""

import itertools
import operator
import collections
import heapq

def sort_by_value(dictionary):
    # dictionary.items()返回一个'list',element是一个个的(key,value) binary tuple.
    # 确切地讲是不是返回list而是dict.items object，这个对象是iterable的，这就像map()返回一个map object一个道理。但是逻辑上完全可以理解成返回list，只是使用上不能当成list使用(不能调用列表方法)
    # 要把dictionary.items()变list,直接再加typecast --> list()就ok了.
    # sorted()的返回值是list,element也就是dictionary.items()的element(i.e. binary tuple)
    result_list = sorted(dictionary.items(),key = operator.itemgetter(1))
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

# Three approaches to traverse an iterable and do some operation for each element: loop, map, list/dictionary comprehension
def traverse_dictionary(dictionary):
    for key in dictionary:
        print('key: ',key,' -> value: ',dictionary[key])
    return
def traverse_dictionary_2(dictionary):
    for key,value in dictionary.items(): #返回一个list,element是一个个的binary tuple。是tuple就可以x, y = (e1,e2)
        print('key: ',key,' -> value: ',value)
    return

def traverse_dictionary_3(dictionary):
    true_false_flag = [print('key: ',key,' -> value: ',value) for key,value in dictionary.items()]
    return true_false_flag #return a list where element indicates whether print() is called successfully.

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
# key procedure/idea is zip(list1,list2): ['a','b'] [1,2] ---> [('a',1),(b,2)]
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

# map(func,iterable) compared with list comprenhension, dictionary comprenhension
# can we pass a function to list comprehension's first parameter? just as in map()'s first parameter.
# The answer is yes! Thus, both function or expression is applicable for the first parameter! see the following example:
# list comprehension is more flexible and functional, because it has a third part: predicate.
# See three parts in list comprehension: https://www.geeksforgeeks.org/python-list-comprehension-and-slicing/
# Lastly, do not forget lambda expression(a.k.a anonymous function) : it is equal to a function.
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
    result_list = sorted(dictionary.items(),key = operator.itemgetter(0))
    dictionary = dict(result_list)
    print(dictionary)
    return dictionary

def sort_by_key_2(dictionary):
    result_list = sorted(dictionary.items(),key = operator.itemgetter(0))
    dictionary = {x:y for x,y in result_list} # x,y means tuple(i.e. (x,y)) 序列解包
    #result_list的element是tuple,是tuple就可以序列解包(sequential unpacking). Thus, we have x,y in result_list.
    print(dictionary)
    return dictionary

def combine_two_dictionary(dict_one,dict_two):   # add two Counter object
    counter_one = collections.Counter(dict_one)  # use constructor to initialize a Counter object
    counter_two = collections.Counter(dict_two)  # Counter object: Counter({'a': 100, 'b': 200, 'c':300})
    result_counter = counter_one + counter_two   # 'a + b' operator  __add__  add(x,y)
    result_dictionary = dict(result_counter)
    print(result_counter)                        # Counter object, Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
    print(result_dictionary)
    return

def char_frequency(input_string): # word frequency is the same idea.
    result_dictionary = {}
    for c in input_string:
        #c = c.lower()
        if c not in result_dictionary:
            result_dictionary[c] = 1
        else:
            result_dictionary[c] += 1
    print(result_dictionary)
    return result_dictionary

# 如果涉及到判断 key 是否存在，则使用get()如果key存在，返回value;如果key不存在则返回第二个函数参数(默认是None)。
def char_frequency_2(input_string):
    result_dictionary = {}
    for c in input_string:
        #c = c.lower()
        result_dictionary[c] = result_dictionary.get(c, 0) + 1  # get()自带‘检查key是否存在’,自带if condition.
    print(result_dictionary)
    return result_dictionary


def char_frequency_3(input_string): # any interable can be function paramter
    #input_string = input_string.lower()
    counter_object = collections.Counter(input_string) # use constructor to initialize a Counter object
    result_dictionary = dict(counter_object)
    print(result_dictionary)
    return result_dictionary

'''
word frequency/char frequency parallel idea:
    divide one file into several files(several pieces)
    for each file:
        readline
        Counter(line)
        update this file's Counter object by: Counter += Counter
    update total file's Counter object by: Counter += Counter
'''

# After counting the character frequency, we can further explorer the top-k items in char frequency dictionary
def top_k_items(input_string,k = 1):     # any interable can be function paramter
    counter_object = collections.Counter(input_string) # use constructor to initialize a Counter object
    char_frequency_dictionary = dict(counter_object)
    result_list = heapq.nlargest(k, char_frequency_dictionary, key = char_frequency_dictionary.get)
    # key = function just as in sorted() map()
    print(result_list)
    return result_list

# 字典名相当于是在针对key eg for d in dictionary 其实是迭代的key 相当于for d in keys(). MIT6.0001
    # dictionary.items()         返回dict_items([('A', 1), ('B', 2), ('C', 3)])  dict_items object, iterable.
    # dictionary.keys()          返回dict_keys(['A', 'B', 'C'])                  dict_keys object, iterable
    # dictionary.values()        返回dict_values([1, 2, 3])                      dict_values object, iteralble
                                 # Not a list, you can test by using list method eg .append() 会报错: AttributeError: 'dict_keys' object has no attribute 'append'
# When accessing a dictionary, you can use either dictionary[key] or dictionary.key

def top_k_items_2(input_string,k = 1):
    counter_object = collections.Counter(input_string) # use constructor to initialize a Counter object
    char_frequency_dictionary = dict(counter_object)
    result_list = heapq.nlargest(k, char_frequency_dictionary.items(), key = operator.itemgetter(1))
    result_dictionary = dict(result_list)
    # heapq.nlargest() 中的'key' parameter is just as 'key' parameter in sorted() map() itertools.groupby()
    print(result_dictionary)
    return result_dictionary

'''
Top K parallel idea:
    divide one file into 100 pieces
    for each piece:
        maintain a priority queue i.e. build a heap
    while(i < K):
        pop from 100 heaps
        select max/min from 100 values
        maintain the heap where max/min value was selected.
'''

def sort_diction_value(dictionary): # not sort by key/value
    result_list = {x:sorted(y) for x,y in dictionary.items()}
    result_dictionary = dict(result_list)
    print(result_dictionary)
    return result_dictionary

def count_success_number(alist):
    generator_g = (d['success'] for d in alist) # 生成器 generator
    print(sum(generator_g))
    return sum(generator_g)

'''
create_defaultdic + sum_function = collections.Counter()
'''
def create_defaultdic(list1,list2): # defaultdict allow for duplicate
    d = collections.defaultdict(list)
    for k,v in zip(list1,list2):    # s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d[k].append(v)              # d[k]不再是value,而是一个list,所以用append()
    return d

def create_defaultdic_2(dict_one,dict_two):
    d = collections.defaultdict(list)   #list set tuple
    for k,v in itertools.chain(dict_one.items(),dict_two.items()):
        d[k].append(v)
    return d

def sum_function(default_dic):
    new_dic = {}
    for k in default_dic:
        new_dic[k] = sum(default_dic[k])
    return new_dic

def sum_function_2(default_dic):
    keys = default_dic.keys()
    values = map(sum,default_dic.values()) #default_dic.values()的每一个value都是一个list
    return {x:y for x,y in zip(keys,values)}


def my_counter():
    l1 = ['yellow','blue','yellow','blue','red']
    l2 = [1,2,3,4,1]
    d1 = create_defaultdic(l1,l2)

    one = {'yellow': 1, 'blue': 2, 'red': 1}
    two = {'yellow': 3, 'blue': 4}
    d2 = create_defaultdic_2(one,two)

    new_dic1 = sum_function(d1) #sum_function_2
    new_dic2 = sum_function(d2) #sum_function_2

    print(new_dic1)
    print(new_dic2)
    return


#------------------------------------------------------------

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
    traverse_dictionary_3(dic_two)
    print(create_dictionary(5))
    print(create_dictionary_2(5))
    print(create_dictionary_3(5))
    print(create_dictionary_4(5))
    print(create_dictionary_5(5))
    print(create_dictionary_6(5))
    list_comprehense()
    print(merge_dictionary(dic_one,dic_two))
    dic_three = dic
    print(delete_dictionary_item(dic_three,'X'))
    sort_by_key(dic)
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    combine_two_dictionary(d1,d2)
    input_string = "Prof. Zhang's research interests include machine learning and its application, particularly in computer vision."
    char_frequency(input_string)
    char_frequency_2(input_string)
    char_frequency_3(input_string)
    top_k_items(input_string,5)
    top_k_items_2(input_string,5)
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    sort_diction_value(num)
    student = [
                {'id': 1, 'success': True, 'name': 'Lary'},
                {'id': 2, 'success': False, 'name': 'Rabi'},
                {'id': 3, 'success': True, 'name': 'Alex'}
            ]
    count_success_number(student)
    my_counter()
    return

if __name__ == '__main__':
    main()
