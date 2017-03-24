## f(t) = a cos(2*Pi*t + b) + c

from scipy.optimize import curve_fit

import pylab as plt

import numpy as np

from math import pi

def mycos(t, a, b, c):
	return a*np.cos(2*pi*t + b) +c

data = np.array(np.loadtxt('Munich_weather.txt', float))

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

for n in temperature:
	nx += 1
	if n <= np.mean(temperature):
		wtemp.append(n)
	else:
		stemp.append(n)

t = np.linspace(2008,2013,nx)

a_guess = np.amax(temperature)


b_guess = 2008

c_guess = np.mean(temperature)

hot = np.mean(stemp)

cold = np.mean(wtemp)


p0 = [a_guess, b_guess, c_guess]

#b####################################

print ("The average temperature in Munich from the beginning of 2008 to the end of 2012 is ", c_guess, " degrees C\n the average summer temperature is ", hot, "degrees C\n the averge winter temperature is ", cold, "degrees C")


#doing a fit
fit = curve_fit(mycos,t,temperature, p0=p0)

#plot first estimate

first_estimate = mycos(t,*p0)

#recreate fit post-op

temp_fit = mycos(t,*fit[0])

##popt, pcov = curve_fit(mycos,x,y)




#timedata = np.linspace(2008,2013,nx)

#temp_guess = mycos(t,*p0)



#tempdata = 




plt.plot(t,temperature,'.')
plt.plot(t,temp_fit, label = 'after fitting')
plt.plot(t,first_estimate, label = 'first guess')
plt.xlim = (2008,2013)
plt.xlabel ("Time after 2008 (years)")
plt.ylabel ("Temperature")
plt.legend()
plt.show()


# a = 


# b = 


# c =



