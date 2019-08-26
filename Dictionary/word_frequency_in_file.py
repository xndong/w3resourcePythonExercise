# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:54:54 2019

@author: Dong Xiaoning
"""
# word frequency in a plain text file

import os
import os.path
import collections

SHAKESPEARE_POEM = 'shakespeare.txt'
TAYLORSWIFT_LYRICS = 'all_tswift_lyrics.txt'

def get_path():
    dirname = os.getcwd()
    file_list = [e for e in os.listdir(dirname) if os.path.isfile(e)]
    return dirname,file_list

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
    dirname,file_list = get_path()
    with open(os.path.join(dirname,TAYLORSWIFT_LYRICS)) as f:
        result_dictionary={}
        for line in f:
            dictionary = word_count_helper(line)
            result_dictionary = combine_dictionary(result_dictionary,dictionary)
    return result_dictionary

def main():
    result = word_count()
    print(result['love'])
    return


if __name__ == '__main__':
    main()
