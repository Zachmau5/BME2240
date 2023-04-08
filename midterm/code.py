
import numpy as np
import matplotlib.pyplot as plt
# load the text file using numpy's loadtxt function
data = np.loadtxt('output2.txt',skiprows=15)

time = data[:,0]
#time=data[15:515]
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

#plt.plot(xpoints, u1points, c="green", label="RK4")

#plt.yscale("log")
# plt.ylabel("Y-Axis")
# plt.xlabel("X-Axis")
# plt.legend()
#plt.title("Euler's, Midpoint, Rk4, and Analytical Solutions for Equation 1")
#plt.text(-0.1, 10**(2.3),"\u0394t = {:.2f}".format(N))



plt.figure(figsize=(15,8))
plt.plot(xpoints, column2, label="Measured")
plt.plot(xpoints, u1points, label="RK4 Analysis")
plt.title("Oscilliating Mass on a Spring")
plt.xlabel("Time (sec)")
plt.ylabel("Height (m)")
plt.legend()
plt.grid()
plt.savefig("fuck a me no fuck a u.png")
plt.show()

# plt.show()
