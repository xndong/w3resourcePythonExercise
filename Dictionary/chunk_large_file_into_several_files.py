# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:53:26 2019

@author: Dong Xiaoning
"""

import os
import os.path

DATA_FILE = 'shakespeare.txt'
DATA_SAVE_FOLDER = 'shakespearedata'
CHUNK_SIZE = 204800 # about 1024KB

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
        number = 0
        filename = str(number).zfill(4)+'.txt'
      # do-while is more readable but unfortunately python does not support this feature.
        chunk = rf.read(CHUNK_SIZE)
        while len(chunk) > 0:
            with open(os.path.join(write_path,filename),'w') as wf:
                wf.write(chunk)
            chunk = rf.read(CHUNK_SIZE)
            number += 1
            filename = str(number).zfill(4)+'.txt'
    return

if __name__ == '__main__':
    main()


