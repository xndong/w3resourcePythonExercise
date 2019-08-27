# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:08:55 2019

@author: Dong Xiaoning
"""

'''
# os:
  # os.system('bash command') 
        # eg bash = 'python test.py arg1 arg2'
        #    os.system(bash)

  # Process Management: these functions may be used to create and manage processes.   ---> https://docs.python.org/3/library/os.html#process-management
    os.execl(path, arg0, arg1, ...)             os.execv(...)
    os.execle(path, arg0, arg1, ..., env)       os.execve(...)
    os.execlp(file, arg0, arg1, ...)            os.execvp(...)
    os.execlpe(file, arg0, arg1, ..., env)      os.execvpe(...)
    os.abort()
    os._exit(n)
       
  # os.popen(command, mode) --->does not work.

# built-in:                 --->does not work.
  # execfile('python_file.py')                  ---> execfile() was removed from Python 3
  # exec('code string or code object')          ---> This function supports dynamic execution of Python code. 
                                                     object must be either a string or a code object. 
                                                     If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). 
                                                     If it is a code object, it is simply executed.   ---> https://docs.python.org/3/library/functions.html#exec
  
# subprocess:
  # subprocess.run('ls -a', shell = True)       # shell = True means 你输入的command string当成bash shell(or any other shell).
     = subprocess.run(['ls','-a'])
  # subprocess.Popen(command, shell = True)     # import subprocess module
  # run()是函数，Popen是class因此上面是在用constructor创建一个object.  ---> from documentation.


主py文件  main.py
import os
import subprocess
import itertools
subprocess.run('python //192.168.1.18/Users/DongXiaoning/Downloads/w3resourcePythonExercise/Dictionary/test.py', shell = True)
for i in itertools.count(10):
    print('Outter process')

另一个py文件 test.py
import itertools
for i in itertools.count(0):
    print('Inner process is running!!!')

结论： 无论是哪种方式os.system(), subprocess.run()....依旧是在sequential running。主进程会阻塞，进入到执行子进程，结束以后再回到主进程。
      因此，这种方法显然不是并发执行(cocurrent)，不是多个进程。
      用多进程来并发其实‘并不好’，因为每个进程都有各自独立的进程空间，彼此不共享，需要进程间通信。
      Instead, we encourage you to use multithread to achieve cocurrent executing.
'''
