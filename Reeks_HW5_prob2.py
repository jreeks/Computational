import fitsio
import os
import numpy as np 
import numpy.ma as ma
from scipy.optimize import curve_fit
import pylab as plt



#load the file

file = 'specObj-dr13.fits'

data = fitsio.FITS(file)

#cut appropriate data

cut = data[1].where('0.4 < SPECTROFLUX[3] - SPECTROFLUX[4] && SPECTROFLUX[3] - SPECTROFLUX[4] <0.45')

subset = data[1][cut]

#Select data to plot
Z = []


ZERR = []
SPEC1 = []
SPEC = []


for k in range(len(subset)):
	Z.append(subset[k]['Z'])
	ZERR.append(subset[k]['Z_ERR'])

	SPEC1.append(subset[k]['SPECTROFLUX'])




Z = np.array(Z)
ZERR = np.array(ZERR)
SPEC1 = np.array(SPEC1)

SPEC = SPEC1[:,3]

# make a mask



#Apply Mask



#Plot Data



#Linear Fit

minit = []
bguess = 0

bdata = 0

for n in range(len(subset) - 1):
	dd = (Z[n+1]-Z[n])/(SPEC[n+1]-SPEC[n])
	minit.append(dd)

	if SPEC[n] == 0:
		bdata = True
		bguess = Z[n]
	else:
		bdata = False

mguess = np.mean(minit)

if bdata == False:

	bguess = Z[4] - (mguess*SPEC[4])

def linear(x,m,b):
	return m*x + b

#doing a fit

p0 = [mguess, bguess]

linfit = curve_fit(linear,Z,SPEC, p0=p0)

#first estimate

first_estimate_lin = linear(Z,*p0)

#recreate fit post-op

zlinfit = linear(Z,*linfit[0])

#quadratic
def quad(x,a,b,c):
	return a*(x**2)+(b*x)+c

#doing a fit

aguess = 1

b2guess = 1

cguess = 1

p0 = [aguess, b2guess, cguess]

qfit = curve_fit(quad,Z,SPEC, p0=p0)

#first estimate

first_estimate_q = quad(Z,*p0)

#recreate fit post-op

zqfit = quad(Z,*qfit[0])



#plot fits

plt.plot(Z,SPEC,'.')

plt.plot(Z,zlinfit, label = 'lin1 after fitting')
plt.plot(Z,first_estimate_lin, label = 'lin1 first guess')
plt.plot(Z,zqfit,',', label = 'quad after fitting')
plt.plot(Z,first_estimate_q,',', label= 'quad first estimate')



plt.xlabel ("SPECTROFLUX[3]")
plt.ylabel ("Z")
plt.legend()
plt.show()

