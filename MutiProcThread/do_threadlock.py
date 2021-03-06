#!/usr/bin/env python3
# coding=utf-8

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('hello %s(in %s)'%(std,threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('huang',),name='Thread-H')
t2 = threading.Thread(target = process_thread,args=('liang',),name = 'Thread-L')
t1.start()
t2.start()
t1.join()
t2.join()

