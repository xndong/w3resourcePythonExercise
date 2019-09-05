# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:08:22 2019

@author: DongXiaoning
"""
iterable = [10,11,12,13,12,12,13,14]

l = []
l = [1]
l = [1,]
l = [iterable]       # equals to l = list(iterable)
l = [iterable,]

t = ()
t = (1)              # int     () ---> operator
t = (1,)             # tuple   () ---> indicate tuple 
t = (iterable)       # equals to t = tuple(iterable)
t = (iterable,)


s = set(iterable)
s = {}     # equals to s = set()  ---> empty set
s = {1}    # equals to s = {1,}
s = {1,2,3,4,2,2,5}
