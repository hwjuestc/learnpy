#!/usr/bin/env python3
# coding=utf-8

'''
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
'''

class Student2(object):
    
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth

class Screen(object):

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,h):
        self._height = h
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,w):
        self._width = w

    @property
    def resolution(self):
        return self._width * self._height

