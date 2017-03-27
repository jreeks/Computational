from math import sqrt

import itertools

v = float(input('What fraction of the speed of light will you travel? (as a decimal: .2, .5, etc.)'))
c = 1
vb = [.9, .98, .999]
beta = (v**2)/(c**2)
gamma = 1/(sqrt(1-(beta**2)))


### (a)

distance = float(input ('How far away is the planet you would like to travel to, in light years?'))



t_earth = distance/v 

t_prime = gamma * v * distance

print (" (a) Your trip will take ", t_earth, " years on earth")

print (" (b) Your trip will take you ", t_prime, " years according to the clock on your ship.")



### b

xb = 10




for k in vb:

	betab = (k**2)/(c**2)
	gammab = 1/(sqrt(1-(betab**2)))
	teb = xb/k

	tpb = gammab * k * xb

	print ("For a speed of ", k, "c it will take ", teb, " earth years and ", tpb, "spaceship years to travel 10 light years")

