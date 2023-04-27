#!/usr/bin/python3
import numpy as np

def linear_least_squares(A, b):
    Q, R = qrgs(A)
    
    #Computes the product of the transpose of Q and the vector b.
    QTB = np.dot(Q.T, b)
    
    # Solve Rx = Q^T b using back substitution
    #computes the number of columns in R, which is the same as the number of unknowns.
    n = R.shape[1]
    #intitialize vector of zeros
    x = np.zeros(n)
    
    #uses back substituiton to start with last row of matrix and use the solution for the last unknow
    #variable to solve for the second last...until all unknowns are solved.
    for i in range(n-1, -1, -1):
        x[i] = QTB[i]
        for j in range(i+1, n):
            x[i] -= R[i, j] * x[j]
        x[i] /= R[i, i]
    
    return x

def qrgs(A):
    #intialize orthogonal matrix w/same shape as A
    Q = np.zeros(A.shape)
    #intialize upper triangle of zeros with shape of #col A x #colA
    R = np.zeros((A.shape[1], A.shape[1]), dtype=np.float64)
    #use gram schmidt alg over matrix A
    for j in range(A.shape[1]):
        #extracs the jth col of A and convert to #
        v = A[:,j].astype(np.float64)
        #nested loop to provide col to jth col
        for i in range(j):
            #dot product
            R[i,j] = np.dot(Q[:,i], A[:,j])
            #subtract proj of jth col onto ith col of A. Stores accordingly
            v -= R[i,j] * Q[:,i]
        #compute norm of remain col
        R[j,j] = np.sqrt(np.sum(v**2))
        #normalized the jth col of v to obtain jth col of Q, divide by norm
        Q[:,j] = v / R[j,j]
    #returns QR decomposed matrix of A    
    return Q, R

def eigen(A, max_iter=5000):
    n = A.shape[0]
    V = np.eye(n)
    s = np.trace(A) / n  # initial shift

    for i in range(max_iter):
        Q, R = qrgs(A - s*np.eye(n))
        A = R @ Q + s*np.eye(n)
        V = V @ Q
        eps=1e-18
        if abs(A[n-1, n-2]) == eps:
            break
        # update shift
        s = np.trace(A) / n
    
    w = np.diag(A)
    
    return w, V
