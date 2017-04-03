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
Z2 = []
Z3 = []

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


#broken linear

minit2 = []
bguess2 = 0

bdata2 = 0

spec2 = []

spec3 = []
minit3 = []

mguess2 = 0
mguess3 = 0


for n in SPEC:
	if n <= 0.5:
		spec2.append(n)
	else:
		spec3.append(n)

for k in range(len(spec2)):
	Z2.append(subset[k]['Z'])
	

	

for k in range(len(spec3)):
	Z3.append(subset[k]['Z'])
	

	


for n in range((len(spec2)) - 1):
	dd2 = (Z2[n+1]-Z2[n])/(spec2[n+1]-spec2[n])
	minit3.append(dd2)

	if spec2[n] == 0:
		bdata2 = True
		bguess2 = Z3[n]
	else:
		bdata2 = False

mguess2 = np.mean(minit2)

if bdata2 == False:

	bguess2 = Z2[4] - (mguess2*spec2[4])


#doing a fit

p0 = [mguess2, bguess2]

linfit3 = curve_fit(linear,Z2,spec2, p0=p0)

#first estimate

first_estimate_lin3 = linear(Z,*p0)

#recreate fit post-op

zlinfit = linear(Z,*linfit3[0])



for n in range((len(spec3)) - 1):
	dd3 = (Z3[n+1]-Z3[n])/(spec3[n+1]-spec3[n])
	minit3.append(dd3)

	if spec3[n] == 0:
		bdata3 = True
		bguess3 = Z2[n]
	else:
		bdata3 = False

mguess3 = np.mean(minit3)

if bdata3 == False:

	bguess3 = Z3[4] - (mguess3*spec3[4])


#doing a fit

p0 = [mguess3, bguess3]

linfit3 = curve_fit(linear,Z3,spec3, p0=p0)

#first estimate

first_estimate_lin3 = linear(Z,*p0)

#recreate fit post-op

zlinfit3 = linear(Z,*linfit3[0])


#make fit


#plot fits

plt.plot(Z,SPEC,'.')

plt.plot(Z,zlinfit, label = 'lin1 after fitting')
plt.plot(Z,first_estimate_lin, label = 'lin1 first guess')
plt.plot(Z,zqfit,',', label = 'quad after fitting')
plt.plot(Z,first_estimate_q,',', label= 'quad first estimate')

plt.plot(Z2,zlinfit2, label = 'lin2 after fitting')
plt.plot(Z2,first_estimate_lin2, label = 'lin2 first guess')


plt.plot(Z3,zlinfit3, label = 'lin3 after fitting')
plt.plot(Z3,first_estimate_lin3, label = 'lin3 first guess')

plt.xlabel ("SPECTROFLUX[3]")
plt.ylabel ("Z")
plt.legend()
plt.show()

