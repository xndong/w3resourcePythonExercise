# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:47:14 2019

@author: DongXiaoning
"""
#formatting output;datetime
import datetime
time=datetime.datetime.now()
date=datetime.datetime.today()
print(time)
print(date)
print(time.strftime("%Y-%m-%d %H:%M:%S"))
