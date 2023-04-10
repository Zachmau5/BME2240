import numpy as np

def det_3x3(x):
    sm1= x[np.ix_([1,2],[1,2])]
    sm2= x[np.ix_([1,2],[0,2])]
    sm3= x[np.ix_([1,2],[0,1])]
    D = x[0,0]*det_2x2(sm1)-x[0,1]*det_2x2(sm2)+x[0,2]*det_2x2(sm3)
    return D

def det_2x2(x):
    D = x[0,0]*x[1,1]-x[1,0]*x[0,1]
    return D

def cramer_2x2(A,B):

    A1 = np.copy(A)
    A2 = np.copy(A)
    
    A1[:,0] = B
    A2[:,1] = B

    x= det_2x2(A1)/det_2x2(A)
    y= det_2x2(A2)/det_2x2(A)

    return (x,y)

def cramer_3x3(A,B):

    A1 = np.copy(A)
    A2 = np.copy(A)
    A3 = np.copy(A)
    
    A1[:,0] = B
    A2[:,1] = B
    A3[:,2] = B

    x= det_3x3(A1)/det_3x3(A)
    y= det_3x3(A2)/det_3x3(A)
    z= det_3x3(A3)/det_3x3(A)

    return (x,y,z)


def main():

#coef = np.array([[a11,a12],
                # [a21,a22]])
#const = np.array([s1,s2])
    coef = np.array([[110,-10,-100],
                     [-10,143,-33],
              [-100,-33,233]])
    const = np.array([1,0,0])


    ans=cramer_3x3(coef,const)
    print("Crammer 3 x 3 : %0.3e, %0.3e, %0.3e" % ans)
   
   
if __name__ == "__main__":
    main()
