# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:56:53 2019

@author: Dong Xiaoning
"""
# word frequency in several plain text files

import os
import os.path
import collections
import time
import csv

DATA_SAVE_FOLDER = 'shakespearedata'

def get_path():
    dirname = os.getcwd()
    data_path = os.path.join(dirname,DATA_SAVE_FOLDER)
    file_list = [e for e in os.listdir(data_path) if os.path.isfile(os.path.join(data_path,e))]
    '''
    Note that everything should be under 'current working directory'
        if os.path.isfile(e)
        e is not under current working directory, thus, we use its absolute path --> os.path.join(data_path,e)
    '''
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

def word_count():
    data_path,file_list = get_path()
    result = {}
    for current_file in file_list:
        with open(os.path.join(data_path,current_file)) as f:
            result_dictionary={}
            for line in f:
                dictionary = word_count_helper(line)
                result_dictionary = combine_dictionary(result_dictionary,dictionary)
            print('current result is: ',result_dictionary)
        result = combine_dictionary(result,result_dictionary)
    return result

def main():
    start_t = time.time()
    result = word_count()
    field_names = ['word','count']
    with open('shakespeare_word_frequency_result.csv','w',newline='') as wf:
        csv_writer = csv.DictWriter(wf,fieldnames = field_names,delimiter = ',')
        csv_writer.writeheader()
        for d in result:
            csv_writer.writerow({'word':d,'count':result[d]})
    end_t = time.time()
    print(result)
    print(result['love'])
    print(f'Total run time is: {end_t - start_t}')
    return

if __name__ == '__main__':
    main()

