#Reeks_HW6.py


#all the imports

import pylab as plt

from numpy import array, linspace




from math import sin, cos, pi, sqrt


#parameters

l = 0.17

g = 9.8

#dw/dt = (g/l)*sin(theta)

#dtheta/dt = w

#a

#initial conditions

theta = [.99*pi]

w = [0]

time = [0]






#step size and number of steps

step = .005

nsteps = 1000

#Euler
for j in range (nsteps):
	if j < 1000:
		time.append((j+1)*.005)
	theta.append(theta[j] + step*w[j])
	k1 = (g/l)*sin(theta[j])
	w.append(w[j] - step*k1)

#1st at midpoint

	theta2 = theta[j+1] + (step/2)*w[j+1]
	k2 = (g/l)*sin(theta[j+1]) 
	w2 = (w[j+1] - (step/2)*k2)

#second
	
	theta3 = theta2 + (step/2)*w2
	k3 = (g/l)*sin(theta2)
	w3 = (w2 - (step/2)*k3)

# final point
	theta4 = theta3 + (step)*w3
	k4 = (g/l)*sin(theta3)
	w4 = (w3 - (step/2)*k4)


	dtheta = (w[j] + (2*w[j+1]) +  (2*w2) + w3)/6
	th = (k1 + (2*k2) + (2*k3) + k4)/6
	theta[j+1] = theta[j] + step*dtheta
	w[j+1] = w[j] - step*th



plt.plot (time,theta)
plt.xlabel ("Time")
plt.ylabel ("Theta (Radians)")

plt.show ()

theta = [-pi/1.99]

wh = [0]


for j in range (nsteps):
	k = (-g/l)*sin(theta[j])
	w2 = wh[j] + k*(step/2)

	theta.append(theta[j] + wh[j-1]*step)
	k1 = (-g/l)*sin(theta[j+1])

	wh.append(w2 + (step*k1))
	theta[j+1] = theta[j] + (step*wh[j])



	

plt.plot (time,theta, label = 'leapfrog')
plt.xlabel ("Time")
plt.ylabel ("Theta (Radians)")
plt.legend()
plt.show ()
