import numpy as np
import sistemas_lineales as sl

def doolittle(n, A, L, b):
    #Matrices PlaceHolder
    mU = np.zeros([n,n])
    mY = np.zeros([n,1])
    mX = np.zeros([n,1])
    '''
    #Formato previo
    mA = A.astype('float64')
    mL = L.astype('float64')
    mB = b.astype('float64')
    '''
    mA = A
    mL = L
    mB = b

    #Paso 1
    mU[0,0] = mA[0,0]/mL[0,0]

    #Paso 2
    for j in range(2,n+1):
        mU[0,j-1] = mA[0,j-1]/mL[0,0]
        mL[j-1,0] = mA[j-1,0]/mU[0,0]
    
    #Paso 3
    for i in range(2,n):

        #Paso 4
        suma = 0
        for k in range(1,i):
            suma += mL[i-1,k-1]*mU[k-1,i-1]

        mU[i-1,i-1] = (1/mL[i-1,i-1])*(mA[i-1,i-1]-suma)

        #Paso 5
        for j in range(i+1,n+1):

            sumaU = 0
            for k in range(1,i):
                sumaU += mL[i-1,k-1]*mU[k-1,j-1]
            
            mU[i-1,j-1] = (1/mL[i-1,i-1])*(mA[i-1,j-1]-sumaU)

            sumaL = 0
            for k in range(1,i):
                sumaL += mL[j-1,k-1]*mU[k-1,i-1]

            mL[j-1,i-1] = (1/mU[i-1,i-1])*(mA[j-1,i-1]-sumaL)

    #Paso 6
    suma = 0
    for k in range(1,n):
        suma += mL[n-1,k-1]*mU[k-1,n-1]

    mU[n-1,n-1] = (1/mL[n-1,n-1])*(mA[n-1,n-1]-suma)

    #Paso 7
    mY[0,0] = mB[0,0] / mL[0,0]

    #Paso 8
    for i in range(2, n+1):

        suma = 0
        for j in range(1,i):
            suma += mL[i-1,j-1]*mY[j-1,0]

        mY[i-1,0] = (1/mL[i-1,i-1])*(mB[i-1,0]-suma)

    #Paso 9
    mX[n-1,0] = mY[n-1,0]/mU[n-1,n-1]

    #Paso 10
    for i in range(n-1,0,-1):

        suma = 0
        for j in range(i+1,n-1):
            suma += mU[i-1,j-1]*mX[j-1,0]

        mX[i-1,0] = (1/mU[i-1,i-1])*(mY[i-1,0]-suma)

    #Paso 11
    return mX

Ar = np.array([[225, 0, -25, 0],
               [0, 175, 0, -125],
               [-225, 0, 275, -50],
               [0, -25, -250, 275]
               ],dtype=float)

Br = np.array([[1400],
               [100],
               [2000],
               [0]
               ],dtype=float)

print(doolittle(len(Ar),Ar,np.identity(len(Ar)),Br))
