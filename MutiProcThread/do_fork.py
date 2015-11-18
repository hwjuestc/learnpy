#!/usr/bin/env python3
# coding=utf-8

import os

print('process(%s)start...'%os.getppid())
pid = os.fork()
if pid ==0:
    print('I am child process(%s) and my parent is (%s)'%(os.getpid(),os.getppid()))
else:
    print('I(%s) just created child process (%s)'%(os.getpid(),pid))

