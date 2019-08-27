# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:46:26 2019

@author: Dong Xiaoning
"""

def travese(setx):
    for s in setx:
        print(s)
    return

def main():
    s1 = {1,2,3,4,5}
    s2 = set(['a','b','c','d','e'])
    s3 = set()                # dictionary use {} as well, thus we use 'set()' to represent empty set
    s1.add(1)
    print(s1)
    s1.add(6)
    print(s1)
    s2.update('f','g')
    print(s2)
    s2.update('a','h')        # update() both element or list/tuple as parameter is okay
    s2.update(['x','y','z'])
    print(s2)                 # add() update()自动去重
    s2.pop()                  # pop() or discard(element)
    print(s2)
    s1.discard(6)
    print(s1)

    # intersection and intersection_update
    # union
    # difference   and difference_update       ---> 可以实现补集合
    s4 = s1.copy()
    s1.discard(5)
    s4.add(6)
    print(s4.intersection(s1))
    s4.intersection_update(s1)  # set is mutable. Of course print(s4.intersection_update(s1)) will get 'None' we have discussed it on MIT 6.0001
    print(s4)
    print(s1.union(s2))
    print(s4.difference(s1.union(s2)))   # empty set : set()
    print(s1.union(s2).difference(s4))

    # issubset
    # issuperset   ---> using operator >= or <= 子集、超集 means 两个集合是否包含，A是否包含B所有的元素
    s1 = {1,2,3,4,5}
    s2 = {1,2,'a'}
    s3 = {1,2,3,'a','b'}
    print(s2 <= s1)
    print(s3 <= s1)
    print(s2 <= s3)


    # clear()
    # copy()
    # max() min() len() ---> built in functions

    return

if __name__ == '__main__':
    main()