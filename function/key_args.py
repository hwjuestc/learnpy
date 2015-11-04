#!/usr/bin/env python3
# coding=utf-8

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('huang',30)
person('liang',35,city='beijing')
person('luo',23,city='chongqing',gender='M')

extra={'city':'chongqing','job':'engineer'}
person('luo',24,**extra)
