#!/usr/bin/env python3
# coding=utf-8

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(100))

def move(n,A,B,C):
    if n==1:
        print('%s-->%s'%(A,C))
        return
    move(n-1,A,C,B)
    print('%s-->%s'%(A,C))
    move(n-1,B,A,C)
move(3,'A','B','C')

