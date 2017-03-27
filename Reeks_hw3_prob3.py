# c - 9v (t/theta)^3 int from 0 to theta/t (x^4*exp(x))/((exp(x)-1)**2)

### a

from pylab import plot, show

from math import exp



def cv(x):
    num = (x**4)*exp(x)

    den = (exp(x)-1)**2
    grand = num/den
    return grand

def trap(x):
    for k in range(1,N):
        s += cv(a+(k*h))
    sa = const*s
    return sa
    
V = 1000

rho = 6.022e-28

d = 428

N = 1000

k = 1.38e-23

T = float(input("What is the Temperature"))



frac = T/d

const = 9*V*rho*k*((frac)**3)
a = 0.0
b = frac

h = (b-a)/N

s = .5*cv(a) + .5* cv(b)

for k in range(1,N):
    s += cv(a+(k*h))

sa = const*s
   
print (h*sa)




### b

temp = [range(5,501,1)]

cvb = []

for n in temp:
    trap(n)
    cvb.append

plot (temp,cvb)
show()  