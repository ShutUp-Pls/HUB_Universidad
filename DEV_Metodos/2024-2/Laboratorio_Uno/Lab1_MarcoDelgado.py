import numpy as np

'''
ACTIVIDAD 1: IMPLEMENTACION DEL METODO
'''

def CroutTri(a): 
    n = len(a)

    # Place Holders
    l = np.zeros([n,n])
    u = np.zeros([n,n])
    z = np.zeros([n,1])
    x = np.zeros([n,1])

    # Paso 1
    l[0,0] = a[0,0]
    u[0,1] = a[0,1]/l[0,0]
    z[0,0] = a[0,n]/l[0,0]

    # Paso 2
    for i in range(1,n-1):
        l[i,i-1] = a[i,i-1]
        l[i,i] = a[i,i]-(l[i,i-1]*u[i-1,i])
        u[i,i+1] = a[i,i+1]/l[i,i]
        z[i,0] = (a[i,n]-(l[i,i-1]*z[i-1,0]))/l[i,i]

    # Paso 3
    l[n-1,n-2] = a[n-1,n-2]
    l[n-1,n-1] = a[n-1,n-1]-(l[n-1,n-2]*u[n-2,n-1])
    z[n-1,0] = (a[n-1,n]-(l[n-1,n-2]*z[n-2,0]))/l[n-1,n-1]

    # Paso 4
    x[n-1,0] = z[n-1,0]

    # Paso 5
    for i in range(n-2,-1,-1):
        x[i,0] = z[i,0]-(u[i,i+1]*x[i+1,0])
    
    # Paso 6
    return x

'''
ACTIVIDAD 2: FUNCION QUE CONSTRUYA 'A' Y 'b' A PARTIR DE 'alpha' Y 'n'
'''

def matriz_a(alpha, n):
    a = np.zeros([n,n])
    for i in range(n): # i -> [0,n-1]
        for j in range(n): # j -> [0,n-1]

            if i == j:
                a[i,j] = np.sin((i+j+2)*alpha)*np.cos((i+j+2)*alpha)

            elif j == i-1 and ((i+1)%2) == 1:
                a[i,j] = -1*np.sin(alpha)

            elif j == i-1 and ((i+1)%2) == 0:
                a[i,j] = np.cos(alpha)

            elif j == i+1:
                a[i,j] = 1
            
            else:
                a[i,j] = 0

    return a

def matriz_b(alpha, n):
    b = np.zeros([n,1])
    for i in range(n): # i -> [0,n-1]
        if (i+1)%2 == 0:
            b[i,0] = np.sin((i+1)*alpha) 
        if (i+1)%2 == 1:
            b[i,0] = np.cos((i+1)*alpha)

    return b

'''
ACTIVIDAD 3: RESOLUCIÓN DEL SISTEMA CON a=1 y n=10
'''

# Parametros dados por el ejercicio
ALPHA = 1
N = 10

A = matriz_a(ALPHA, N)
#print(f"Matriz A construida:\n{A}")

B = matriz_b(ALPHA, N)
#print(f"Matriz B construida:\n{B}")

AB = np.concatenate((A, B), axis=1)
#print(f"Matriz Ampliada:\n{AB}")

X = CroutTri(AB)
#print(f"Solucion encontrada:\n{X}")

'''
ACTIVIDAD 3: CALCULO DEL ERROR RELATIVO
'''
b_real = B
#print(f"B Real:\n{b_real}")

b_estimado = np.dot(A,X)
#print(f"B Estimado:\n{b_estimado}")

error_relativo = abs(b_real-b_estimado)/abs(b_real)
print(f"Error Relativo:\n{error_relativo}")

'''
ACTIVIDAD 3: Justificación
- Analicemos el Error Relativo para el vector 'B':

[[8.21927290e-16]
 [2.44193592e-16]
 [0.00000000e+00]
 [2.93398352e-16]
 [1.95694576e-16]
 [1.19201300e-15]
 [1.95694576e-16]
 [1.19201300e-15]
 [1.47263524e-16]
 [2.24432965e-16]
 [1.21851185e-16]
 [0.00000000e+00]]

Un error relativo individual en cada componente del vector 'B'
en el orden de 10^-16 aproximadamente, es lo suficientemente
bajo para considerarse una buena aproximación.

Podemos decir que el vector 'X' encontrado por el algoritmo
nos permite el calcular un vector 'B' muy similar
al vector 'B' construido desde su definición.

Por lo tanto, concluimos que el algoritmo proporciona una buena
aproximación para los valores 'n' y 'alpha' en particular.
'''