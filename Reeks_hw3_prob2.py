# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:20:11 2017

@author: Baby Face
"""


from math import sqrt



### a


a = float(input("What is the value of a?") )

b = float(input("What is b?"))

c = float(input("What about c?") )

x = ((-b)+sqrt((b**2)-(4*a*c)))/(2*a)



y = ((-b)-sqrt((b**2)-(4*a*c)))/(2*a)

print (" ")
print ("your would-be-solutions are ",x, "and ",y)


### b

x = (2*c)/((-b)+sqrt((b**2)-(4*a*c)))

y = (2*c)/((-b)-sqrt((b**2)-(4*a*c)))

print ("for part b you get ", x," and ", y, "This difference comes from errors produced in subtraction of floating points")

coef = [str(a),str(b),str(c)]

for k in coef:
    if float(k)%1 == 0:
        k = int(float(k))
        k = str(k)
        k += ".0"
        k = float(k)
    elif float(k)%1 != 0:
        k += "0"

x = (2*c)/((-b)+sqrt((b**2)-(4*a*c)))

y = (2*c)/((-b)-sqrt((b**2)-(4*a*c)))


print ("the correct values are: ",x, " and ", y)