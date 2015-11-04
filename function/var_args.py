#!/usr/bin/env python3
# coding=utf-8

def power(x,n):
    s=1
    while n>0:
        s = s*x
        n = n-1
    return s
print(power(3,4))
def enroll(name,gender,age='678'):
    print(name,gender,age,id(age))
    print(id(age))
enroll('huang',5)
enroll('huang',5)
enroll('huang',5,'789')
enroll('huang',5,'890')

def add_end(l=[]):
    l.append('end')
    return l
print(add_end())
print(add_end())

def cacl(*numbers):
    sum = 0;
    for num in numbers:
        sum = sum + num*num
    return sum
print(cacl(1,2,3,4))
print(cacl(1,2,3,4))
