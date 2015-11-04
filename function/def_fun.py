#!/usr/bin/env python3
# coding=utf-8

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
#print(my_abs(-1,2))
#print(my_abs('a'))
#print(abs('a'))

import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny
r = move(100,100,60,math.pi/6)
print(r)

def quadratic(a,b,c):
    return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
x = quadratic(1,3,-4)
print(x)
