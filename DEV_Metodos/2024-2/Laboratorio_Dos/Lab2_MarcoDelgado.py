import numpy as np

'''
ACTIVIDAD 1: IMPLEMENTACION DEL METODO
'''

def metodo_sor(n, a, b, xo, w , tol, max):

    # PlaceHolders
    x = np.zeros([n,1])

    # Paso 1
    k = 1

    # Paso 2
    while k <= max:

        # Paso 3
        for i in range(n):

            sum1 = 0
            for j in range(i-1):
                sum1 += a[i,j]*x[j,0]

            sum2 = 0
            for j in range(i+1,n):
                sum2 += (a[i,j]*xo[j,0])

            term1 = (1-w)*xo[i,0]
            term2 = (1/a[i,i])*(w*(-sum1-sum2+b[i,0]))

            x[i] = term1 + term2

        # Paso 4
        x_dif = x-xo
        if abs(np.linalg.norm(x_dif, ord=np.inf)) < tol:
            return x
        # Paso 5
        k += 1

        # Paso 6
        for i in range(n):
            xo[i,0] = x[i,0]
    
    # Paso 7
    return 'número máximo de iteraciones excedido'

'''
ACTIVIDAD 2: PLANTEAR EL PROBLEMA COMO 'AX=B'
'''

def matriz_a(l, h, dif_x):
    # PlaceHolder Matriz A
    n_nodos = int(l/dif_x)
    a = np.zeros([n_nodos, n_nodos])

    # Coeficiente de la diagonal
    coef = 2 + (h*(dif_x**2))

    # Posicionamiento de los coeficientes
    for i in range(len(a)):
        for e in range(len(a[0])):
            if i == e:
                a[i,e] = coef
            elif e == i+1 or e == i-1:
                a[i,e] = -1
    return a

def vector_b(l, ta, t0, tn, h, dif_x):
    # PlacerHolder Vector b
    n_nodos = int(l/dif_x)
    b = np.zeros([n_nodos, 1])

    # Coeficiente del vector
    coef = h*(dif_x**2)*ta

    # Coeficiente al principio
    coef_ini = coef+t0

    # Coeficiente al final
    coef_fin = coef+tn

    # Posicionamiento de los coeficientes
    for i in range(len(b)):
        if i == 0:
            b[i,0] = coef_ini
        elif i == len(b):
            b[i,0] = coef_fin
        else:
            b[i,0] = coef

    return b

'''
De esta forma el sistema se puede expresar como Ax=b
donde 'x' corresponde a las temperaturas de los nodos
'A' Matriz tridiagonal y 'b' vector con primer y último
coeficiente afectado por la condición de la frontera
'''

'''
ACTIVIDAD 3: RESOLVER EL SISTEMA DEL APARTADO ANTERIOR
'''
# Tolerancia
tol = 1e-13
# Numero maximo de iteraciones
n_max = 1000
# Longitud de la barra
l = 10
# Longitud entre nodos
dif_x = 2
# Numero de nodos
n_nodos = int(l/dif_x)
# Vector nulo basado en el numero de nodos
xo = np.zeros([n_nodos, 1])
# Temperatura circundante a la barra
ta = 20
# Temperatura al principio de la barra
t0 = 40
# Temperatura al final de la barra
tn = 200
# Coeficiente de tranferencia de calor
h = 0.02

# Construimos la matriz A y el vector b para el sistema
matriz = matriz_a(l, h, dif_x)
vector = vector_b(l, ta, t0, tn, h, dif_x)

# Valores propios de la matriz
valores_propios = np.linalg.eigvals(matriz)
# Radio espectral de la matriz
radio_espectral = max(abs(valores_propios))
# Selección optima para w
w = 2/(1+np.sqrt(1-(radio_espectral**2)))
print(w)
'''
Al parecer tengo problemas con el calculo del 'w'
daré un valor arbitrario para la resolución
'''
w = 1.5

resultado = metodo_sor(n_nodos, matriz, vector, xo, w, tol, n_max)

print(resultado)