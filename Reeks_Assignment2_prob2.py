
a1 = 15.67
a2 = 17.23
a3 = .75
a4 = 93.2

Z = float(input("What is the atomic number of the atom?"))

A = float(input("What is the atomic mass number of the atom?"))

if A%2 != 0:
	a5 = 0

elif A%2 == 0 and Z%2 == 0:
	a5 = 12.0
else:
	a5 = -12.0





B = (a1*A) - (a2*(A**(2/3))) - (a3*(Z**2)/(A**(1/3))) - ((a4*(A-(2*Z))**2)/A) - (a5/(A**1/2))

bpn = B/A 
print ('The binding energy of this atom is ',B, ' MeV')
print ('The binding energy per nucleon is',bpn,' MeV')