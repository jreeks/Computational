import fitsio
import os
import numpy as np 
import numpy.ma as ma



file = 'specObj-dr13.fits'

data = fitsio.FITS(file)

cut = data[1].where('SPECTROFLUX[3] <0.4 &&  SPECTROFLUX[4] < 0.45)')

subset = data[1][cut]


