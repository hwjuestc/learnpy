#!/usr/bin/env python3
# coding=utf-8


class Student(object):
    def __init__(self):
        self.name = 'HUANG'

    def __getattr__(self,attr):
        if attr=='score':
            return 99

