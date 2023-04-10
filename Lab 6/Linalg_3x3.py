import numpy as np

A=[[1100,-100,-1000],
   [ -100,1430,-330],
   [ -1000,-330,2330]]

s=[1,
   0,
   0]

A_inv = np.linalg.inv(A)

x = np.dot(A_inv,s)

print(x)

x = np.linalg.solve(A,s)

print(x)
