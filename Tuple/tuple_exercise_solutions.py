# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:41:09 2019

@author: DongXiaoning
"""
import collections
import operator

def create_tuple():
    tup_one = 1,2,3,4
    tup_two = 'a',[1,2],'love',{'name':'john','age':26}
    return tup_one,tup_two

# unpack a.k.a. 序列解包
def unpack_tuple():
    tuplex = (1,2,3,4) # tuplex = 1,2,3,4
    print(tuplex)
    a,b,c,d = tuplex
    print(f'a = {a}, b = {b}, c = {c}, d = {d}')

def tuple_to_string(tuplex):  # wrong solution
    return str(tuplex)

def tuple_to_string_2(tuplex):
    return "".join([str(t) for t in tuplex])

# string.join(string)
# tuplex = (1,2,3,4)
# tupley = ('1','2','3','4')

def tuple_to_string_3(tuplex):
    result = ''
    for t in tuplex:
        result += str(t)
    return result

def add_item(tuplex,item):
    alist = [t for t in tuplex]
    alist.append(item)
    tuplex = tuple(alist)
    return tuplex

def indexing(tuplex):
    return tuplex[3],tuplex[-3]

def find_repeat(tuplex):
    result = []
    # string = tuple_to_string_2(tuplex)
    dictionary = collections.Counter(tuplex)
    for k in dictionary:
        if dictionary[k] >= 2:
            result.append(k)
    return result

def find_repeat_2(tuplex):
    result = []
    for t in tuplex:
        if tuplex.count(t) > 1:  # tuple.count()
            result.append(t)
    return list(set(result)) # 去重

def convert_to_tuple(alist):
    return tuple(x for x in alist) # generator. list comprehension

def remove_item(tuplex,item):
    listx = list(tuplex) # 转成list, list的method很多，完成后再转回去
    listx.remove(item)
    return tuple(listx)

def convert_to_dict(tuplex):
    return {x:y for x,y in tuplex} #dictionary comprehension

def convert_to_dict_2(tuplex):
    result = {}
    for x,y in tuplex:
        result[x] = y
    return result

def convert_to_dict_3(tuplex):
    return dict(tuplex)

def unzip_tuple(alist):
    x = [t for t,s in alist]
    y = [s for t,s in alist]
    print(x)
    print(y)
    return x,y
def remove_empty(alist):  # alist = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    return [t for t in alist if t]

def sort_tuple(alist):
    return sorted(alist,key = sort_tuple_helper)       # reversed = True
def sort_tuple_helper(iterable):
    return iterable[1]

def sort_tuple_2(alist):
    return sorted(alist, key = operator.itemgetter(1)) # reversed = True

def main():
    t1,t2 = create_tuple()
    print(t1,t2)
    unpack_tuple()
    tuplex = (1,2,3,4)
    print(tuple_to_string_2(tuplex))
    print(tuple_to_string_3(tuplex))
    print(add_item(tuplex,5))
    print(indexing(tuplex))
    tuplex = (1,1,2,3,3,'x','y','y','z')
    print(find_repeat(tuplex))
    print(find_repeat_2(tuplex))
    alist = [1,1,2,3,3,'x','y','y','z']
    print(convert_to_tuple(alist))
    print(remove_item(tuplex,'x'))
    tuplex = ((2, "w"),(3, "r"))
    print(convert_to_dict(tuplex))
    print(convert_to_dict_2(tuplex))
    print(convert_to_dict_3(tuplex))
    alist = [(1,2), (3,4), (8,9)]
    unzip_tuple(alist)
    alist = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    print(remove_empty(alist))
    alist = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    print(sort_tuple(alist))
    print(sort_tuple_2(alist))
    return


if __name__ == '__main__':
    main()

