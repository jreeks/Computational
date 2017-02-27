# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:36:12 2017

@author: Baby Face
"""

from random import random 
from numpy import array

from pylab import plot, ylim, xlim, show, xlabel, ylabel, show
from numpy import linspace



pb = 0       
            
L2 = 0.69314718   

halfpb = 198
 
halfbi = 2760
 
halfti = 132
    

npb = []

Bi2 = 0
nBi2 = []

Ti = 0
nTi = []

Bi = 10000
nBi = []

gammapb = L2/halfpb

gammabi = L2/halfbi

gammati = L2/halfti


s = []

    
for x in range (0,20001,1):
    s.append(x)     
    npb.append(pb)
    nBi2.append(Bi2)
    nTi.append(Ti)
    nBi.append(Bi)

    for n in range (0,Bi+1):
             
        r = random()
        if r < gammabi:
            b = random()*100
            if b <  97.91: 
                Bi -= 1
                
                pb += 1
                
                
            else:
                Bi -= 1
                Ti += 1
    
    
    
    for n in range(0,pb+1):
        r = random()
        if r < gammapb:
            pb -= 1
            
            Bi2 += 1
            
    
    for n in range (0,Ti+1):
       r = random()
       if r < gammati:
           Ti -= 1
           pb += 1 
        
    


        
plot (s,nBi)
xlim (0,20000)

xlabel ("Time (s)")
ylabel ("Atoms of Bi 213")
show ()
    
plot (s,nTi)
xlim (0,20000)

xlabel ("Time (s)")

ylabel ("Atoms of Ti")
show()
    
plot (s,npb)
xlim (0,20000)

xlabel ("Time (s)")
ylabel ("Atoms of Pb")
show()
    
plot (s,nBi2)
xlim (0,20000)

xlabel ("Time (s)")
ylabel ("Atoms of Bi 206")
show()
    
    
        
    

