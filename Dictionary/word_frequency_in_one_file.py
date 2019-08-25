# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:54:54 2019

@author: Dong Xiaoning
"""
# word frequency in a plain text file

import os
import os.path
import collections
import operator

def get_path():
    shakespeare_data_path = os.path.abspath(__file__)
    dirname, basename = os.path.split(shakespeare_data_path)
    file_list = [e for e in os.listdir(dirname) if os.path.isfile(e)]
    return dirname,basename,file_list


def main():
    get_path()
    return

if __name__ == '__main__':
    main()
