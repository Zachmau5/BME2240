# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:10:17 2023

@author: halle
"""
import numpy as np
from sympy import Matrix

def linear_least_squares(A, b):
    Q, R = qrgs(A)
    
    # Compute Q^T b
    QTB = np.dot(Q.T, b)
    
    # Solve Rx = Q^T b using back substitution
    n = R.shape[1]
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = QTB[i]
        for j in range(i+1, n):
            x[i] -= R[i, j] * x[j]
        x[i] /= R[i, i]
    
    return x

def qrgs(A):
    Q = np.zeros(A.shape)
    R = np.zeros((A.shape[1], A.shape[1]), dtype=np.float64)
    
    for j in range(A.shape[1]):
        v = A[:,j].astype(np.float64)
        for i in range(j):
            R[i,j] = np.dot(Q[:,i], A[:,j])
            v -= R[i,j] * Q[:,i]
        R[j,j] = np.sqrt(np.sum(v**2))
        Q[:,j] = v / R[j,j]
        
    return Q, R
def eigen(A):
    m = Matrix(A)
    eigenvectors = []
    eigenvalues = []
    for eigenvalue, multiplicity, eigenvects in m.eigenvects():
        eigenvalues += [eigenvalue]*multiplicity
        for eigenvect in eigenvects:
            eigenvectors.append(list(eigenvect))
    return eigenvalues, eigenvectors


# def eigen(A, eps=1e-18, max_iter=100):
#     n = A.shape[0]
#     V = np.eye(n)
#     s = np.trace(A) / n  # initial shift

#     for i in range(max_iter):
#         Q, R = qrgs(A - s*np.eye(n))
#         A = R @ Q + s*np.eye(n)
#         V = V @ Q
#         if abs(A[n-1, n-2]) < eps:
#             break
        
#         # update shift
#         s = np.trace(A) / n
    
#     w = np.diag(A)
    
#     return w, V

A = [[10,2,3], [3,12,5], [5,5,8]]
w, V = eigen(A)
print(w)  
print(V)
