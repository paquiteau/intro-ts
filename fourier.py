#!/usr/bin/env python3

import numpy as np

import matplotlib.pyplot as plt

def creneau(x,amp=1,per=5):
    if x%per <= per/2:
        return amp
    return -amp

def triangle(x,amp=1,per=5):
    if x%per <= per/2:
        return (x%per)*4/per-amp
    return amp - (x%per-per/2)*4/per



x = np.linspace(0,10,num=500);
y=np.array(list(map(creneau,x)))
plt.plot(x,y)


def decomp_creneau(x,n,per=5):
    decomp = np.zeros(np.size(x));
    for k in range(1,n+1,2):
       decomp += 1/k*np.sin(2*np.pi*k*x/per)
    return decomp*4/np.pi
       
A = x
iters= [1,3,5,15,50,100]
for n in iters:
    y=decomp_creneau(x,n)
    A=np.vstack([A,y])
    plt.plot(x,y)

head='x,'+str(iters)[1:-1]
np.savetxt('creneau.csv',A.T,fmt='%.5f',delimiter=',',header=head,comments='')
plt.grid()
plt.show()