import numpy as np

def func(x): pass

'''
ACTIVIDAD 1: IMPLEMENTACION DEL METODO
'''

def metodo(a, b, func_c, func_d, func, m, n):
    #Paso 1
    h = (b-a)/n
    j1 = 0
    j2 = 0
    j3 = 0

    # Paso 2
    for i in range(n+1): #i\in[0,n]
        # Paso 3
        x = a + (i*h)
        hx = (func_d(x) - func_c(x))/m
        k1 = func(x, func_c(x)) + func(x, func_d(x))
        k2 = 0
        k3 = 0
        
        # Paso 4
        for j in range(1,m): #j\in[1,m-1]
            # Paso 5
            y = func_c(x) + (j*hx)
            q = func(x,y)

            # Paso 6
            if j%2 == 0: k2 += q
            else: k3 += q
        
        # Paso 7
        l = ((k1 + (2*k2) + (4*k3))*hx)/3

        # Paso 8
        if i == 0 or i == n: j1 += l
        else:
            if i%2 == 0: j2 += l
            else: j3 += l

    # Paso 9
    j = (h*(j1 + (2*j2) + (4*j3)))/3

    # Paso 10
    return j
    
'''
ACTIVIDAD 2: ENCONTRAR EL CENTRO DE MASA PARA LA LAMINA
'''
# Funcion de densidad dada por el problema
# usaremos k=1 como valor arbitrario
def fd(x, y, k=1): return k

# Funciones a integrar
def fx_1(x, y): return x*fd(x, y)
def fx_2(x, y): return fd(x, y)

def fy_1(x, y): return y*fd(x, y)
def fy_2(x, y): return fd(x, y)

# Limites de integracion para x
a = 0
b = 1

# Limites de integracion para y
def y1(x): return 0
def y2(x): return np.exp(x)

# Enteros n,m dados por el problema
n = 14
m = n

# Aplicamos simpson para encontrar el centro de masa
x_aprox = metodo(a, b, y1, y2, fx_1, m, n)/metodo(a, b, y1, y2, fx_2, m, n)
y_aprox = metodo(a, b, y1, y2, fy_1, m, n)/metodo(a, b, y1, y2, fy_2, m, n)

print(f"Centro de masa según Simpson:{float(x_aprox),float(y_aprox)}")

'''
ACTIVIDAD 2: COMPARAR ERRORES RELATIVOS
'''

# Centro de masa definido en la actividad
x = 1/(np.exp(1)-1)
y = (np.exp(1)+1)/4

print(f"Centro de masa según actividad:{float(x),float(y)}")

# Error realitvo entre ambos resultados
erx = (abs(x-x_aprox)/x)*100
ery = (abs(y-y_aprox)/y)*100

print(f"\nError relativo porcentual para cada parametro:")
print(f"Error de \'x\'= {erx}%")
print(f"Error de \'y\'= {ery}%")

# Un error relativo porcentual muy pequeño
# Aproximación por el metodo relativamente buena