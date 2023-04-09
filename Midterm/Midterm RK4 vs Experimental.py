# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:32:38 2023

@author: halle
"""


import numpy as np
import matplotlib.pyplot as plt
# load the text file using numpy's loadtxt function
data = np.loadtxt('output2.txt',skiprows=15)

time = data[:,0]
column2 = data[:, 1]
col2=(((column2[0:500])/1000)-0.23)
column2=((column2)/1000)
column2=column2-0.232


c=0.02
m=0.74#mag
k=56 #freq
g=9.8

def Func(u1, u2, x):
    return (-((c/m)*u2)-((k/m)*u1)+g)

A =60
B= 0
N =1483
D = (A-B)/N


#xpoints = time
xpoints=np.arange(B,A,D)
u2points = []
u1points = []

u1=0
u2=0

for x in xpoints:
    u1points.append(u1)
    u2points.append(u2)

    m1 = D*u2
    k1 = D*Func(u1, u2, x)  #(x, v, t)

    m2 = D*(u2 + 0.5*k1)
    k2 = D*Func(u1+0.5*m1, u2+0.5*k1, x+0.5*D)

    m3 = D*(u2 + 0.5*k2)
    k3 = D*Func(u1+0.5*m2, u2+0.5*k2, x+0.5*D)

    m4 = D*(u2 + k3)
    k4 = D*Func(u1+m3, u2+k3, x+D)

    u1 += (m1 + 2*m2 + 2*m3 + m4)/6
    u2 += (k1 + 2*k2 + 2*k3 + k4)/6


plt.figure(figsize=(15,8))
plt.plot(xpoints, column2,'o',c='green', label="Measured")
plt.plot(xpoints, u1points, label="RK4 Analysis",c='red')
plt.title("RK4 vs Measured Mass on a Spring")
plt.xlabel("Time (sec)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid()
plt.savefig("RK4 vs Measured.png")
plt.show()

# plt.show()
