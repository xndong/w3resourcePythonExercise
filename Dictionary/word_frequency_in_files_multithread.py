# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:35:22 2019

@author: Dong Xiaoning

time.sleep(n)
start_t = time.time()
end_t = time.time()
total_time = end_t - start_t

------------------------Notes from python documentation 3.7.4--------------------------------

Queue
Pipe
Shared memory

inherite Thread object

->threading module:

# threading.current_thread() # return a thread object  ---> current running thread object
# threading.currentThread()  # an alias
# threading.get_ident()      # get thread's indentifier

# Thread class:
  thread_object = threading.Thread(target,args) # constructor
  thread_object.start()
  thread_object.join()
  thread_object.is_alive()
  thread_object.name

# Lock class:
  threading.Lock()        # constrcutor
  lock_object.acquire()   # mutex, lock, thread_mutex, thread_lock can be as good varible names
  lock_object.release()

-> multiprocessing module:

#
#
# Pipe class
# Queue class    # In general, it is just a clone of queue.Queue 
  queue_object = multiprocessing.Queue(maxSize)             # constrcutor
  queue_object.empty()
  queue_object.full()
  queue_object.put()
  queue_object.get()

# Process class:
  process_object = multiprocessing.Process(target,args)      # constructor
  process_object.start()
  process_object.join()
  process_object.name
  process_object.pid
  process_object.kill()
  process_object.close()

# Lock class:
  multiprocessing.Lock()        # constructor
  lock_object.acquire()         # mutex, lock, process_mutex, process_lock can be as good varible names
  lock_object.release()
"""
# word frequency in several plain text files with multi-thread

import os
import os.path
import time
import collections
import threading
import multiprocessing

DATA_SAVE_FOLDER = 'shakespearedata'
THREAD_NUM = 8

def get_path():
    dirname = os.getcwd()
    data_path = os.path.join(dirname,DATA_SAVE_FOLDER)
    file_list = [e for e in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,e))]
    return data_path,file_list

def preprocess(string):
    result_list = [c.lower() for c in string if c.isalpha() or c == ' ']
    result_string = "".join(result_list)
    return result_string
def word_count_helper(string):
    string = preprocess(string)
    alist = string.split(' ')
    counter_object = collections.Counter(alist)
    dictionary = dict(counter_object)
    return dictionary

def combine_dictionary(dic_one, dic_two):
    return collections.Counter(dic_one) + collections.Counter(dic_two)

def word_count(file_list,queue):
    thread_name = threading.currentThread().name
    thread_identifier = threading.get_ident()
    print(f'current running thread is: {thread_name}, thread identifier is: {thread_identifier}') # yet another format io
    dirname = os.getcwd()
    data_path = os.path.join(dirname,DATA_SAVE_FOLDER)
    result = {}
    for current_file in file_list:
        with open(os.path.join(data_path,current_file)) as f:
            result_dictionary={}
            for line in f:
                dictionary = word_count_helper(line)
                result_dictionary = combine_dictionary(result_dictionary,dictionary)
            print('current result is: ',result_dictionary)
            time.sleep(0.5)
        result = combine_dictionary(result,result_dictionary)
    queue.put(result)
    return result

'''
 This main function seems not very elegant, so I change it into main_2, main_3 and main_4.
 I am not sure whether lock is necessary. I think it is in main thread. So it is not necessary. 
    # That is true.
 We can check if there is difference in running results.
'''
def main():
    start_t = time.time()
    result = {}
    data_path,file_list = get_path()
    queue = multiprocessing.Queue()
    threads = []
    # lock = threading.Lock()
    for thread_i in range(THREAD_NUM):
        file_list_part = [file_list[idx] for idx in range(len(file_list)) if idx % THREAD_NUM == thread_i ]
        thread = threading.Thread(target = word_count,args =(file_list_part,queue))
        threads.append(thread)
        thread.start()
        # lock.acquire()
        result = combine_dictionary(result,queue.get())
        # lock.release()
    for thread in threads:
        thread.join()
    end_t = time.time()
    print(result)
    print(result['love'])
    print(f'Total run time is: {end_t - start_t}')
    return

def main_2():
    start_t = time.time()
    result = {}
    data_path,file_list = get_path()
    queue = multiprocessing.Queue()
    threads = []
    for thread_i in range(THREAD_NUM):
        file_list_part = [file_list[idx] for idx in range(len(file_list)) if idx % THREAD_NUM == thread_i ]
        thread = threading.Thread(target = word_count,args =(file_list_part,queue))
        threads.append(thread)
        thread.start()
    for i in range(THREAD_NUM):
        result = combine_dictionary(result,queue.get())
    for thread in threads:
        thread.join()
    end_t = time.time()
    print(result)
    print(result['love'])
    print(f'Total run time is: {end_t - start_t}')
    return

def main_3():
    start_t = time.time()
    result = {}
    result_list =[]
    data_path,file_list = get_path()
    queue = multiprocessing.Queue()
    threads = []
    # lock = threading.Lock()
    for thread_i in range(THREAD_NUM):
        file_list_part = [file_list[idx] for idx in range(len(file_list)) if idx % THREAD_NUM == thread_i ]
        thread = threading.Thread(target = word_count,args =(file_list_part,queue))
        threads.append(thread)
        thread.start()
        # lock.acquire()
        result_list.append(queue.get()) # 你是在做append(),显然加不加锁都一样。实验验证:结果一样，running time也几乎一样。
        # lock.release()
    for thread in threads:
        thread.join()
    for e in result_list:
        result = combine_dictionary(result,e)
    end_t = time.time()
    print(result)
    print(result['love'])
    print(f'Total run time is: {end_t - start_t}')
    return

def main_4():
    start_t = time.time()
    result = {}
    result_list =[]
    data_path,file_list = get_path()
    queue = multiprocessing.Queue()
    threads = []
    for thread_i in range(THREAD_NUM):
        file_list_part = [file_list[idx] for idx in range(len(file_list)) if idx % THREAD_NUM == thread_i ]
        thread = threading.Thread(target = word_count,args =(file_list_part,queue))
        threads.append(thread)
        thread.start()
    for thread_i in range(THREAD_NUM):
        result_list.append(queue.get()) # 你是在做append(),显然加不加锁都一样。实验验证:结果一样，running time也几乎一样。
    for thread in threads:
        thread.join()
    for e in result_list:
        result = combine_dictionary(result,e)
    end_t = time.time()
    print(result)
    print(result['love'])
    print(f'Total run time is: {end_t - start_t}')
    return

if __name__ == '__main__':
    main_4()