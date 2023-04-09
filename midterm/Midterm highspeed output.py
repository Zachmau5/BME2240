# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:57:46 2023

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

A =60
B= 0
N =1483
D = (A-B)/N


#xpoints = time
xpoints=np.arange(B,A,D)
plt.figure(figsize=(15,8))
plt.plot(xpoints, column2, label="Measured")
plt.title("Highspeed Camera Output of Mass on a Spring")
plt.xlabel("Time (sec)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid()
plt.savefig("Highspeed_Camera_Output.png")
plt.show()

