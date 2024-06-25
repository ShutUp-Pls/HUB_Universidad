import ecuaciones as ec

from ASCII_Tabla import generate_dict, print_ascii_table
from math import pi

FX = ec.f2
P0 = ec.P1_F2

TOL = 1e-20
N_MAX = 100

def derivar(f, x, h=1e-10): return (f(x + h) - f(x - h)) / (2 * h)

# Metodo 1:1 a las indicaciones del BURDEN
def newton(fx,p0,tol,n):

    # Paso 1
    i = 1

    # Paso 2
    while i <= n:

        # Paso 3
        p = p0-(fx(p0)/derivar(fx,p0))

        # Paso 4
        if abs(p-p0) < tol:
            return p
        
        # Paso 5
        i += 1

        # Paso 6
        p0 = p
    
    return print(f"El metodo fracasó después de {n} iteraciones")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def newton_descriptivo(fx,p0,tol,n):
    l0 = ["n","p"]
    l1,l2 = [],[]
    i = 0
    while i <= n:

        l1.append(i)
        l2.append(p0)

        p = p0-(fx(p0)/derivar(fx,p0))
        if abs(p-p0) < tol:
            print(f"El metodo supera la tolerancia despues de {i} iteraciones.")
            return generate_dict(l0,l1,l2)
        i += 1
        p0 = p
    print(f"El metodo falla despues de {i} iteraciones.")
    return generate_dict(l0,l1,l2)

print_ascii_table(newton_descriptivo(FX,P0,TOL,N_MAX))