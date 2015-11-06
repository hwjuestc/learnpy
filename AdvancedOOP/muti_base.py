#!/usr/bin/env python3
# coding=utf-8

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass



class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal,RunnableMixIn):
    pass


class Bat(Mammal,FlyableMixIn):
    pass
