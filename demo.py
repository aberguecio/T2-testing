from ast import *

def bla(x):
    y = 0
    return y

def bla2(a):
    b = 0
    if True:
        c = 0
        d = a
    return c

def bla3():
    pass
class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def fullName(self):
        return self.firstName + self.lastName