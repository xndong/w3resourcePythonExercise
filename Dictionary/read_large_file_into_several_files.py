# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:31:01 2019

@author: Dong Xiaoning

csv:
    with open(xxx) as rf:              # raw file object rf(iterable object).
        csv_reader = csv.reader(rf)    # Note that we have two read-related class: reader(rf) DictReader(rf) etc to help you obtain a higer lerve read object.
        for line in csv_reader:        # _csv.reader object ---> csv_reader(iterable object).
            print(csv_reader)          

    csv.reader()         csv.writer()
    csv.DictReader()     csv.DictWriter()   # 使用了DicWriter()则csv_writer的写入内容必须是dictionary-style format: either dictionary or DicReader()读的东西
                                            # 使用了DicReader()则csv_reader读出来的line就是dictionary-style format

all attrbutes and methods in csv module:
    import csv
    dir(csv)

"""

# read csv lyric data set
# split into several files in a directory

import os
import os.path
import csv

DATA_FILE = 'songdata.csv'
FIELD_NAMES = ['artist','song','link','text']
DATA_SAVE_FOLDER = 'songdata'   # path: directory or file; folder: folder

def get_path():
    dirname = os.getcwd()
    data_path = os.path.join(dirname,DATA_FILE)
    return dirname,data_path


def main():
    dirname, read_path = get_path()
    write_path = os.path.join(dirname,DATA_SAVE_FOLDER)
    if not os.path.exists(write_path):
        os.mkdir(write_path)
    with open(read_path,'r') as rf:
        csv_reader = csv.DictReader(rf)
        is_open = False
        for line in csv_reader:
            if not is_open:
                wf = open(os.path.join(write_path,line['artist']+'.txt'),'w')
                is_open = True
                artist = line['artist']
                print(artist)
              # print("Generating {}'s lyrics".format(artist))
            if line['artist'] != artist:
                wf.close()
                is_open = False
                continue
            wf.write(line['text'])
    return

if __name__ == '__main__':
    main()

