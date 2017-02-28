# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:47:37 2017

@author: johnreeks
"""
# I = integral (x**(-.5)/(exp(x)+1)) from 0..1

#

from math import sqrt, exp
from numpy import linspace, array
from random import random


def w(x):
    return 1/(sqrt(x))
    
    

def f(x):
    return (x**(-.5))/(exp(x)+1)

steps = 1000000 

xmin = 0.00000001
xmax = 1.0





fx = []


hit = 0

pv = []
x = []




def p(x):
    return 1/(2*(sqrt(x)))      
        



numpoints = 1000000


for n in linspace (0.000001,1,1000000):
    fx.append (f(n))    
    pn = p(n)    
    pv.append (pn)
    x.append (n)
    

    
for i in range (1,numpoints):
    
    x2 = x[int(random()*i)]
    y = pv[i]
    
    if f(x2) > y:
        hit += 1




perhit = hit/numpoints

I = perhit

print (I)      
    
        
        












   



#for k in x:
#    w.append(sqrt(x))
    
    








