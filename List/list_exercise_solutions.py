# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:18:25 2019

@author: Dong Xiaoning
"""
import itertools
import operator


def sum(alist):
    sum = 0
    for list_element in alist:
        sum += list_element
    return sum


def mul(alist):
    mul = 1
    for list_element in alist:
        mul = mul * list_element
    return mul


def mul_recursive(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        new_start = alist[0]
        new_list = alist[1:]
        return new_start * mul_recursive(new_list)


def max(alist):
    max = 0
    for element in alist:
        max = (max, element)[element > max]  #trinary expression in python
    return max


def problem_6_solution(alist):
    result_list = []
    for list_element in alist:
        if not result_list:
            result_list.append(list_element)
        else:
            for index, element in enumerate(result_list):
                if list_element[1] < element[1]:
                    result_list.insert(index, list_element)  #修改了列表，所以上面的 in 会被破坏。 remember MIT 6.0001
                    break                                    # because we mutate our result_list, thus we violate our interator. Finally, endless loop will occur.
    return result_list


def remove_duplicate(alist):
    dictionary = {}.fromkeys(alist)
    return list(dictionary.keys())


def remove_duplicate_2(alist):
    return list(set(alist))


def common_member(alist_one, alist_two):
    aset_one = set(alist_one)
    aset_two = set(alist_two)
    aset_result = aset_one.intersection(aset_two)
    print(aset_result)
    if len(aset_result):
        return True
    return False


def list_comprehension():
    return [x for x in range(100) if x % 5 == 0 and x**2 < 500]


#permuation   a.k.a.排列
#combination  a.k.a.组合
def permutation(alist):
    astring = ""
    return permutation_helper(alist, astring)


def permutation_helper(alist, astring):
    #base case
    if len(alist) == 0:
        print("This is:", astring)
    #backtracking a.k.a traceback
    #recursive case
    else:
        #backtracking: choose-explore-unchoose
        for index, element in enumerate(alist):
            #choose
            astring += str(element)
            #explore
            alist.remove(element)
            permutation_helper(alist, astring)
            #unchoose
            astring = astring[:-1]
            alist.insert(index, element)
    return "All permutation has been printed out."


def sub_set(alist):
    chosen = []
    return sub_set_helper(alist, chosen)


def sub_set_helper(alist, chosen):
    #base case
    if (len(alist) == 0):
        print(chosen)
    #recursive case
    else:
        #backtracking: choose - explore - unchoose
        #choose 'with'
        pop_element = alist.pop(0)
        chosen.append(pop_element)
        #explore
        sub_set_helper(alist, chosen)
        #unchoose
        alist.insert(0, chosen[-1])
        chosen.pop(-1)

        pop_element = alist.pop(0)
        #choose 'without'
        #explore
        sub_set_helper(alist, chosen)
        #unchoose
        alist.insert(0, pop_element)


def map_test():
    l = [1, 2, 3, 4]
    l2 = l * 2
    print("Raw l: ", l)
    print("Raw l2: ", l2)
    print(str(l))
    result = "".join(map(str, l))  # 对l中每个element做str操作(str是一个函数名，和sorted()等函数一样，这里同样相当于在做transform)，返回一个'map object'
    print("First join: ", result, "string length is: ", len(result))
    #map object is iterable
    result = "".join(str(l))       # 对l做str操作，返回一个str object.
    print("Second join: ", result, "string length is: ", len(result))


def generator_test():
    l = [1, 2, 3, 4]
    x = (str(e) for e in l)             # something called 'tuple comprehension '? No, x actually is a 'generator object' i.e.由generator(生成器)生成的object——一切皆对象.
    for element in x:                   # generator is iterable
        print(element)
    print(
        ''.join(x))                     #迭代器耗尽，所以这里print不出来。just comment the above two lines code
    print(''.join(str(c) for c in l))   #重新来一次迭代

    #stringFoo1.join(Foo2)
    #Foo2 can be any iterable object, but element in Foo2 must be string, thus:
    # list,tuple,dictionary,string(of course string itself is also included) --- commonly used
    # generator object
    # map object
    #is also okay.


def circularly_identical(list_one, list_two):
    string_one = "".join(map(str, list_one))
    string_two = "".join(map(str, list_two * 2))
    return (False, True)[string_one in string_two]


def element_concatenate(list_one, list_two):
    result_list = ['{}{}'.format(i, j) for i in list_one for j in list_two]
    return result_list


def element_concatenate_2(list_one, list_two):
    result_list = []
    iterable = itertools.product(list_one, list_two)            # Combinatoric iterators产生的interable object的element是用tuple来表示的。
    for element in iterable:
        element = "".join(map(str, element))                    #element = "".join(str(e) for e in element)
        result_list.append(element)
    return result_list


# itertools(iterator tools):
# Infinite iterators
# Iterators terminating on the shortest input sequence --- chain, compress, groupby, islice
# Combinatoric iterators --- product, permutations, combinations


def sort_metric(element):  # count the numbers of char 'A'. 以包含字符'A'的数目为标准来排序.
    number = 0
    for e in element:
        if e == 'A':
            number += 1
    return number


def sort_function(alist):
    # alist在排序时，其比较的方式不是alist的元素之间直接比，而是alist的元素进入key函数之后的返回值来进行比较。
    # key函数就是一种映射或者just as transform into Z space
    # parameter 'key = xxx' can be saved, it is not mandatory.
    result_list = sorted(alist, key=sort_metric)  #sorted()函数返回list类型,其element是alist(can be any iterable object)的element
    print(result_list)
    result_list = sorted(alist, key=operator.itemgetter(0))  # 以index = 0 的元素来排序
    print(result_list)
    '''
    operator.itemgetter(0)返回一个callable object i.e. we can call it(like a funtion). As python official doc says,
    its parameter is an any iterable object. Here, every element in alist will be passed into operator.itemgetter(0)
    and get a 'return value'.
    
    Usage:
        l=[1,2,3,4,5,6,7,8]
        operator.itemgetter(0)(l)
    '''


def main():
    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum(alist))
    print(mul(alist))
    print(mul_recursive(alist))
    print(max(alist))
    alist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(problem_6_solution(alist))
    alist = [1, 2, 3, 4, 5, 6, 7, 2, 4, 7, 8, 9, 4, 3, 2, 5, 7, 7]
    print(remove_duplicate(alist))
    print(remove_duplicate_2(alist))
    print(common_member(alist, [6, 7, 100]))
    print(list_comprehension())
    alist_number = [1, 2, 3]
    alist = ['a', 'b', 'c']
    print(permutation(alist_number))
    print(permutation(alist))
    print(sub_set(alist))

    map_test()
    generator_test()

    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    print(circularly_identical(list1, list2))

    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3, 4]
    print(element_concatenate(list1, list2))
    print(element_concatenate_2(list1, list2))

    alist = [
        'A', 'BCDE', 'AA', 'ARARAR', 'BBBAAA', 'AAAA', 'EFGHIJKL', 'AE', 'E',
        'F'
    ]
    sort_function(alist)

    word_list = [
        'be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see',
        'come', 'think', 'look', 'want', 'give', 'use', 'find', 'tell', 'ask',
        'work', 'seem', 'feel', 'leave', 'call'
    ]
    # key = function可以还可以用在排序sorted(),以及map()
    for letter, words in itertools.groupby(
            sorted(word_list), key = operator.itemgetter(0)):
        print(letter)
        for word in words:
            print(word)


if __name__ == '__main__':
    main()
