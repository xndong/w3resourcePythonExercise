# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:18:22 2019

@author: DongXiaoning
"""
# Motivation of numpy:
# In scientific computing, we need lots of computation among scalar, vector, matrix...etc.  However, list only has limited methods for us to use.
# i.e. list(raw built-in compounded data type, a.k.a collections) is not enough for us to deal with scientific computing. Thus ,we introduce numpy. 
# In numpy, a new data type called ndarray(n dimension array) is presented, and we have 1-dimension arry, 2-dimension array, 3-dimension array...etc.
# ndarry(everything is an object in python) expands raw list to an extrem extent, which provides bunches of methods for you to use.
# Please feel free to explore how to use ndarry just as what you did in learning to use raw built-in collections(string,list,tuple,set,dictionary,heap/priority queue)

# numpy has attractive features:
  # faster and save storage space than list
  # functional than list
  # can be backend of some modules eg pandas  ---> pandas encapsulates numpy and provides higher level interface and operations

import numpy as np
'''
basic attributes and operations of ndarray object
'''
# create ndarray(n-dimension array) from list
a = np.array([1,2,3,4,5,6])
# ndarray object
type(a)
# data type: dtype. We have default dtype in each method of creating/initializing ndarray.
b = np.array([4,5,6],dtype = 'float')
# get dimension
a.ndim
# get shape
a.shape     # ----> output is a tuple object
# get size
a.itemsize
a.size
# get array storage size/ total size
a.nbytes # equal to a.size * a.itemsize
# get type ---> data type: dtype ---> int8,16,32,64  uint8,16,32,64 float16,32,64 complex64,128 bool_
a.dtype
# to list
a.tolist()
# to string etc
a.tostring()
'''
access: read, write, modify, silcing, indexing, replacing ---> just as what we do in list
# using indexing and silcing to replace or modify a block area.
# slicing is reference, so be careful as what we do while copy.
# slicing steps [start:end:step]
'''
a[1]
a[0:3]

'''
 more function in numpy module to create/initializing ndarry.
 # data type ---> dtype always can be specified.
 # shape (2,3,4) is explicit ---> of course, you can also use 'b.shape' implicitly.
 # xx_like() ---> take ndarray object as the first parameter.
'''
np.zeros(10)                            # one-dimension array (1-d array, 1d array in the following)
np.zeros((5,5))                         # 2d array
np.zeros((2,3,4))                       # 3d array
np.zeros((2,3,4,5))                     # 4d array
np.zeros(a.shape)
np.ones((2,3),dtype = 'float')          # 1d array and specify data type: dtype
np.full((2,3),100,dtype ='float')       # 2d array and initial value is 100
np.full_like(a,100)                     # full_like take ndarray object as the first parameter
# random number 
np.random.rand(5,5)
np.random.random_sample(a.shape)
np.random.randint(1,100,(5,))           # 5,  1.
np.random.randint(1,100,(5,5))          # np.random.rand...
# indentity --> 单位矩阵
np.identity(10)
# creat an array by repeating
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0) # repeat 3 times and repeat on axis 0 ---> axis 0 是 [1,2,3] thus repeat it 3 times
# Be careful when copying data.
# You are encouraged to use copy() method, instead of point to the same thing.
a = np.zeros(5)
b = a       # use b = a.copy() ---> give a real copy in memory.
b[0] = 9
print(a)    # a[0] has been changed



'''
operations: + - * / ** ---> all of this operations are elementwise
'''
arr = np.array([1,2,3,4,5,6,7])
start = 0
stop = 100
num = 10
step = 20
a = np.linspace(start,stop,num,endpoint = True) # default true 
b = np.arange(start,stop,step)
# 1-d array  + - * / %  scalar        #  all are elementwise.
# 1-d array  + - * / %  1-d array
# 1-d array  + - * / %  2-d array
# 2-d array  + - * / %  scalar
# 2-d array  + - * / %  2-d array
# broadcast can be used when doing these opeartions
np.add()
np.subtract()
np.multiply()
np.division()
np.sqrt()
np.power()
# universal functions a.k.a. ufuncs
np.sin(arr)
np.cos(arr)
np.min(arr)
np.max(arr)
np.sum(arr)
np.mean(arr)
np.std(arr)

'''
linear algebra ---> we are not doing elementwise!
               ---> we have all linear algebra operations 
'''
x1 = np.ones((2,3),dtype = 'int')
x2 = np.full((3,2),10,dtype = 'int')
a = np.identity(5)
b = np.random.rand(5,10)
# linear algebra computation
np.matmul(x1,x2)   # ----> matrix multiply, equals to np.dot(x1.transpose(),x2)   because x1.transpose().transpose() == x1
np.dot(a,b)        # ----> matrix multiply, but transpose a first
                   #       equals to np.matmul(a.transpose(),b)
                   #       np.dot本来来自向量內积inner product，we expand it to matrix
np.inner(a,b)      # ----> totally equals to np.dot(a,b)

np.linalg.det(a)   # 求矩阵的秩
# linalg:
# determinant
# trace
# sigular vector decompostion
# inverse
# matrix norm
# 啥都有，乔列斯基分解都有....

'''
reorganize arrays
'''
arr = np.array([1,2,3,4])
arr.reshape((2,2))
# stack
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
np.vstack(v1,v2)
h1 = np.ones((2,2))
h2 = np.ones((2,4))
np.hstack(h1,h2)
np.concatenate((a1,a2,a3),axis = 0)  # default axis = 0

# Note that axis is a very useful parameter in many functions or methods, it provide you a fine grained operation on ndarray

'''
FileIO, sterilization(持久化)
Numpy binary files, Text files, Raw binary files...
'''
np.genfromtxt()         # from text files
np.load()               # from numpy binary files
np.loads()
np.loadtxt()
np.save()
np.savetxt()
np.savez()
np.savez_compressed()


'''
element data type cast
'''
arr.astype('int32')
np.int16(arr)

'''
boolean masking and advanced indexing
'''
arr > 5         # ----> i.e. (arr > 5)
((arr > 1) & (arr < 5))
arr[arr > 5]    # arr > 5 as index, return value of whose index is True. ----> i.e. arr[(arr > 5)]
arr[[arr > 5]]  # ----> use arr[(arr > 5)] instead, see the following information
'''
FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; 
  use `arr[tuple(seq)]` instead of `arr[seq]`. 
In the future this will be interpreted as an array index, `arr[np.array(seq)]`, 
  which will result either in an error or a different result.
'''
arr[[1,3,5]]  #[1,3,5]  as index for 1 d array    ---> index [1] [3] [5]
              #[1,3,5]  as index for 2 d array    ---> index [1] [3] [5] i.e. the 2nd, 4th, 5th row.
arr[[1,3,5],[1,3,5]]  #[1,3,5],[2,4,6] as index for 2 d array ---> index [1][2] [3][4] [5][6]
np.any(arr > 0, axis = 0) # whether is ture or not ? axis 0 上,用arr > 0去mask,是否存在(any)元素？ 
np.all(arr > 0, axis = 0) # return True or False

mask1 = arr > 5  # mask = condition expression
mask2 = arr.max()
np.where(mask1)   # ---> return indices of True   tuple object
np.where(mask2)   # ---> return indices of True   tuple object 
# index (pl.)---> indices






















# Motivation of numpy:
# In scientific computing, we need lots of computation among scalar, vector, matrix...etc.  However, list only has limited methods for us to use.
# i.e. list(raw built-in compounded data type, a.k.a collections) is not enough for us to deal with scientific computing. Thus ,we introduce numpy. 
# In numpy, a new data type called ndarray(n dimension array) is presented, and we have 1-dimension arry, 2-dimension array, 3-dimension array...etc.
# ndarry(everything is an object in python) expands raw list to an extrem extent, which provides bunches of methods for you to use.
# Please feel free to explore how to use ndarry just as what you did in learning to use raw built-in collections(string,list,tuple,set,dictionary,heap/priority queue)

# numpy has attractive features:
  # faster and save storage space than list
  # functional than list
  # can be backend of some modules eg pandas  ---> pandas encapsulates numpy and provides higher level interface and operations

import numpy as np
'''
basic attributes and operations of ndarray object
'''
# create ndarray(n-dimension array) from list
a = np.array([1,2,3,4,5,6])
# data type: dtype. We have default dtype in each method of creating/initializing ndarray.
b = np.array([4,5,6],dtype = 'float')
# get dimension
a.ndim
# get shape
a.shape
# get size
a.itemsize
a.size
# get array storage size/ total size
a.nbytes # equal to a.size * a.itemsize
# get type ---> data type: dtype
a.dtype
'''
access: read, write, modify, silcing, indexing, replacing ---> just as what we do in list
using indexing and silcing to replace or modify a block area.
'''
a[1]
a[0:3]

'''
 more function in numpy module to create/initializing ndarry.
 # data type ---> dtype always can be specified.
 # shape (2,3,4) is explicit ---> of course, you can also use 'b.shape' implicitly.
 # xx_like() ---> take ndarray object as the first parameter.
'''
np.zeros(10)                            # one-dimension array (1-d array, 1d array in the following)
np.zeros((5,5))                         # 2d array
np.zeros((2,3,4))                       # 3d array
np.zeros((2,3,4,5))                     # 4d array
np.zeros(a.shape)
np.ones((2,3),dtype = 'float')          # 1d array and specify data type: dtype
np.full((2,3),100,dtype ='float')       # 2d array and initial value is 100
np.full_like(a,100)                     # full_like take ndarray object as the first parameter
# random number 
np.random.rand(5,5)
np.random.random_sample(a.shape)
np.random.randint(1,100,(5,))           # 5,  1.
np.random.randint(1,100,(5,5))          # np.random.rand...
# indentity --> 单位矩阵
np.identity(10)
# creat an array by repeating
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0) # repeat 3 times and repeat on axis 0 ---> axis 0 是 [1,2,3] thus repeat it 3 times
# Be careful when copying data.
# You are encouraged to use copy() method, instead of point to the same thing.
a = np.zeros(5)
b = a       # use b = a.copy() ---> give a real copy in memory.
b[0] = 9
print(a)    # a[0] has been changed


'''
operations: + - * / ** ---> all of this operations are elementwise
'''
arr = np.array([1,2,3,4,5,6,7])
# 1-d array + - * / scalar        #  all are elementwise
# 1-d array + - * / 1-d array
# 1-d array + - * / 2-d array
# 2-d array + - * / scalar
# 2-d array + - * / 2-d array
np.add()
np.subtract()
np.multiply()
np.division()

np.sin(arr)
np.cos(arr)
np.min(arr)
np.max(arr)
np.sum(arr)
np.mean(arr)
np.std(arr)

'''
linear algebra ---> we are not doing elementwise!
               ---> we have all linear algebra operations 
'''
x1 = np.ones((2,3),dtype = 'int')
x2 = np.full((3,2),10,dtype = 'int')
a = np.identity(5)
b = np.random.rand(5,10)
# linear algebra computation
np.matmul(x1,x2)   # ----> matrix multiply, equals to np.dot(x1.transpose(),x2)   because x1.transpose().transpose() == x1
np.dot(a,b)        # ----> matrix multiply, but transpose a first
                   #       equals to np.matmul(a.transpose(),b)
                   #       np.dot本来来自向量內积inner product，we expand it to matrix
np.inner(a,b)      # ----> totally equals to np.dot(a,b)

np.linalg.det(a)   # 求矩阵的秩
# linalg:
# determinant
# trace
# sigular vector decompostion
# inverse
# matrix norm
# 啥都有，乔列斯基分解都有....

'''
reorganize arrays
'''
arr = np.array([1,2,3,4])
arr.reshape((2,2))
# stack
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
np.vstack(v1,v2)
h1 = np.ones((2,2))
h2 = np.ones((2,4))
np.hstack(h1,h2)

'''
FileIO, sterilization(持久化)
'''
np.genfromtxt()
np.load()
np.loads()
np.loadtxt()
np.save()
np.savetxt()
np.savez()
np.savez_compressed()


'''
element data type cast
'''
arr.astype('int32')
np.int16(arr)

'''
boolean masking and advanced indexing
'''
arr > 5
((arr > 1) & (arr < 5))
arr[arr > 5]  # arr > 5 as index
arr[[1,3,5]]  #[1,3,5]  as index for 1 d array    ---> index [1] [3] [5]
arr[[1,3,5],[1,3,5]]  #[1,3,5],[2,4,6] as index for 2 d array ---> index [1,2] [3,4] [5,6]
np.any(arr > 0, axis = 0)
np.all(arr > 0, axis = 0)