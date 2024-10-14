import numpy as np
import sistemas_lineales as sl

A = sl.A_5
B = sl.B_5

AB = np.concatenate((A, B), axis=1)
N = AB.shape[0]

def metodo_gauss(n = None, A = None):
    #Necesario si se usan funciones que requieran compatibilidad de datos como "+=" o ".add"
    A = A.astype('float64')

    #Paso 1: Triangularizar matriz
    for i in range(1,n):

        #Paso 2: Verificar la existencia de un pivote (Primer numero en columna distinto de 0)
        p = -1
        for k in range(i, n+1):
            if A[k-1,i-1] != 0:
                p = k
                break
        if p == -1: return print("Pivote no encontrado")

        #Paso 3: Si el pivote no está en la diagonal, lo movemos
        if p != i: A[[p-1,i-1]] = A[[i-1,p-1]]

        #Paso 4: Hacer 0 los valores bajo el pivote
        for j in range(i+1,n+1):

            #Paso 5: Calculamos el multiplicador
            m = A[j-1,i-1]/A[i-1,i-1]

            #Paso 6: Se realiza la operacion elemental fila
            A[j-1] += (-m*A[i-1])

    #Paso 7: Verificamos que el valor del ultimo pivote es distinto de 0
    if A[n-1,n-1] == 0: return print("No existe solucion unica")

    #Paso 8: Definimos el primer valor de X encontrado
    x = np.zeros((n,1))
    x[n-1,0] = A[n-1,n]/A[n-1,n-1]

    #Paso 9: Encontramos los demas valores de X
    for i in range (n-1, 0, -1):
        sum = 0
        for j in range(i+1,n+1): sum += A[i-1,j-1]*x[j-1,0]
        x[i-1,0] = (1/A[i-1,i-1])*(A[i-1,n]-sum)
    
    #Paso 10: Retorna la solución del sistema
    return x

print(metodo_gauss(N, AB))