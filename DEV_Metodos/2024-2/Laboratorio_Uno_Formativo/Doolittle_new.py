import numpy as np

def doolittle(a, l, b):
    n = len(a)
    x = np.zeros([n,1])
    y = np.zeros([n,1])
    u = np.zeros([n,n])

    # Paso 1
    u[0,0] = a[0,0]/l[0,0]

    # Paso 2
    for j in range(1, n):
        u[0,j] = a[0,j]/l[0,0]
        l[j,0] = a[j,0]/u[0,0]
    
    # Paso 3
    for i in range(1,n-1):

        # Paso 4
        sum = 0
        for k in range(0,i):
            sum += l[i,k]*u[k,i]
        u[i,i] = (1/l[i,i])*(a[i,i]-sum)

        #Paso 5
        for j in range (i,n):
            sum = 0
            for k in range(0,i):
                sum += l[i,k]*u[k,j]
            u[i,j] = (1/l[i,i])*(a[i,j]-sum)
            sum = 0
            for k in range(0,i):
                sum += l[j,k]*u[k,i]
            l[j,i] = (1/u[i,i])*(a[j,i]-sum)
        
    # Paso 6
    sum = 0
    for k in range(0,n-1):
        sum += l[n-1,k]*u[k,n-1]
    u[n-1,n-1] = (1/l[n-1,n-1])*(a[n-1,n-1]-sum)

    # Paso 7
    y[0,0] = b[0,0]/l[0,0]

    # Paso 8
    for i in range(1,n):
        sum = 0
        for j in range(0,i):
            sum += l[i,j]*y[j,0]
        y[i,0] = (1/l[i,i])*(b[i,0]-sum)

    # Paso 9
    x[n-1] = y[n-1]/u[n-1,n-1]

    # Paso 10
    for i in range(n-2,-1,-1):
        sum = 0
        for j in range(i,n):
            sum += u[i,j]*x[j,0]
        x[i,0] = (1/u[i,i])*(y[i,0]-sum)
        
    return x

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

print(doolittle(Ar,np.identity(len(Ar)),Br))