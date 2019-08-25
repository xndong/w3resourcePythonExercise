# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:05:04 2019

@author: Dong Xiaoning

datetime:
    datetime.datetime.fromtimestamp(timestamp)  eg st_mtime
os: print(dir(os))
    path --> directory or file.
    os.environ.get('HOME')
    os.uname()
    os.getcwd(path)                         # file
    os.listdir(path)
    os.chdir(path)                          # directory  It will change current working directory to your path
    os.mkdir(path)                          # directory
    os.mkdirs(path)                         # directorys
    os.rmdir(path)  a.k.a. os.removedir()   # directory
    os.removedirs(path)                     # directorys
    os.rename(path)                         # file
    os.stat(path)                           # file
    os.stat(path).st_mtime
    os.getenv()
    os.putenv()
    os.walk(path)                           # directory  Deep-first traverse(该函数自动进行递归，不必手写)   It will return path, dirnames and filenames
os.path:
    os.path.abspath(path)
    os.path.relpath(path)

    os.path.split(path)
    os.path.splitdrive()
    os.pathsplitext()
    os.path.dirname()
    os.path.basename()
    os.path.join()

    os.path.commonpath()
    os.path.commonprefix()

    os.path.exists(path)

    os.path.expanduser(path)

    os.path.isfile()
    os.path.isdir()

    os.path.getatime()
    os.path.getmtime()
    os.path.getctime()
os: FileIO
    f = open(path,'rwb')    # open  a file and obtain a file object f. Note that open() is the alias of file()
    print(dir(f))
    print(f.mode)
    f.close()
  # using context manager a.k.a.上下文管理器 to automatically close f file object.
    f.read()
    f.read(chunk_size)
    f.readline()
    f.readlines()    # return a list
    f.tell()
    f.seek(n)        # walk to position n
    f_line = f.readline()
    print(f_line, end = '') # youtube to avoid additional 换行 
    f.write()
    with open(xxx) as rf:               # copy就是从一个file读，然后写到另一个file里。Thus, 我们首先打开两个file.
        with open(xxx) as wf:
            for line in rf:
                wf.write(line)
"""


