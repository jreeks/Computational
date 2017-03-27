## f(t) = a cos(2*Pi*t + b) + c

from scipy.optimize import curve_fit

import pylab as plt

import numpy as np

import numpy.ma as ma

from math import pi

def mycos(t, a, b, c):
	return a*np.cos(2*pi*t + b) +c

data = np.array(np.loadtxt('Munichweather.txt', float))

#a###########################

print ("The significance of the parameters are: \na is the amplitude \nb is the phase shift \nc is the offset")



nx = 0



temperature = []

stemp = []

ind = 0

wtemp = []


#generate time and temperature arrays and count number of points

data = data[np.logical_not(np.logical_or(data[:,0] < 2008, data[:,0]>=2013))]

temperature = data[:,1]

# mask outliers 

m_temp = ma.masked_outside(temperature, 30, -20, copy = True)



for n in m_temp:
	nx += 1
	if n <= np.mean(m_temp):
		wtemp.append(n)
	else:
		stemp.append(n)

t = np.linspace(2008,2013,nx)



a_guess = np.amax(m_temp)


b_guess = 2008

c_guess = np.mean(m_temp)

hot = np.mean(stemp)

cold = np.mean(wtemp)


p0 = [a_guess, b_guess, c_guess]

#b####################################

print ("The average temperature in Munich from the beginning of 2008 to the end of 2012 is ", c_guess, " degrees C\n the average summer temperature is ", hot, "degrees C\n the averge winter temperature is ", cold, "degrees C")


#doing a fit
fit = curve_fit(mycos,t,m_temp, p0=p0)

#plot first estimate

first_estimate = mycos(t,*p0)

#recreate fit post-op

temp_fit = mycos(t,*fit[0])

#plot data

plt.plot(t,m_temp,'.')
plt.plot(t,temp_fit, label = 'after fitting')
plt.plot(t,first_estimate, label = 'first guess')
plt.xlim = (2008,2013)
plt.xlabel ("Time after 2008 (years)")
plt.ylabel ("Temperature")
plt.legend()
plt.show()

#print coefficients
print ('a, b, and c are ', *fit[0], ' respectively')

