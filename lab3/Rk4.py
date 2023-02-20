import numpy as np
import matplotlib.pyplot as plt

#def function
def func(x,y):
    return ((y*x*x)-(y*x)-y)

#intial conditions
x0=0
y0=1
k1=func(x0,y0)


xf = 4
stp = 0.01
n = int((xf-x0)/stp + 1)

x=np.linspace(x0,xf,n)
#Establishing blank arrays as numpy does weird shit trying to create an array and compute
#Euler
yEuler=np.zeros([n])
k1Euler=np.zeros([n])

#Midpoint
yMidpt=np.zeros([n])
k1Midpt=np.zeros([n])
k2Midpt=np.zeros([n])

#.....RK4
yRK4=np.zeros([n])
k1RK4=np.zeros([n])
k2RK4=np.zeros([n])
k3RK4=np.zeros([n])
k4RK4=np.zeros([n])


#set inital condition for calculation
yEuler[0]=y0
k1Euler[0]=k1

#set itial for midpoint
yMidpt[0] = y0
k1Midpt[0] = k1
k2Midpt[0] = func(y0+stp/2, y0+stp/2*k1)

#and..Rk4
yRK4[0] = y0
k1RK4[0] = k1
k2RK4[0] = func(y0 + stp/2, y0 + stp/2*k1)
k3RK4[0] = func(y0 + stp/2, y0 + stp/2*k2RK4[0])
k4RK4[0] = func(y0 + stp, y0 + stp*k3RK4[0])


#Filling in said arrays. Substantially easier than trying to locate certain cells in excel
for i in range(1,n):
    yEuler[i]=stp*(k1Euler[i-1]) + yEuler[i-1]
    k1Euler[i]=func(x[i], yEuler[i])
    
    yMidpt[i]=stp*( k2Midpt[i-1] ) + yMidpt[i-1]
    k1Midpt[i] = func(x[i], yMidpt[i])
    k2Midpt[i] = func(x[i] + stp/2, yMidpt[i] + stp/2*k1Midpt[i])
    
    yRK4[i] = stp*( k1RK4[i-1]/6 + k2RK4[i-1]/3 + k3RK4[i-1]/3 + k4RK4[i-1]/6) + yRK4[i-1]
    k1RK4[i] = func(x[i], yRK4[i])
    k2RK4[i] = func(x[i] + stp/2, yRK4[i] + stp/2*k1RK4[i])
    k3RK4[i] = func(x[i] + stp/2, yRK4[i] + stp/2*k2RK4[i])
    k4RK4[i] = func(x[i] + stp, yRK4[i] + stp*k3RK4[i])
    
#plotting this dAta    
plt.plot(x, yEuler, ":", c="darkorange", label="Euler")
plt.plot(x, yMidpt, ':', c="grey", label="Midpoint")
plt.plot(x,yRK4, ':', c="gold", label="RK4")
xval=np.linspace(x0, xf, 1000)
analytical=(np.e**(xval**3/3-xval**2/2-xval))
plt.plot(xval, analytical,"-",c="steelblue", label="Analtical")
plt.yscale("log")
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")
plt.legend()
plt.title("Euler's, Midpoint, Rk4, and Analytical Solutions for Equation 1")
plt.text(-0.1, 10**(2.3),"\u0394t = {:.2f}".format(stp))
plt.show()
