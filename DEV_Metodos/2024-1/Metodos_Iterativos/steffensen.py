from ASCII_Tabla import generate_dict, print_ascii_table

import ecuaciones as ec

GX = ec.g4
P0 = 1.5

TOL = 1e-3
N_MAX = 100

# Metodo 1:1 a las indicaciones del BURDEN
def steffensen(gx,p0,tol,n):

    # Paso 1
    i = 1

    # Paso 2
    while i <= n:

        # Paso 3
        p1 = gx(p0)
        p2 = gx(p1)
        p = p0-(((p1-p2)**2)/(p2-(2*p1)+p0))

        # Paso 4
        if abs(p-p0) < tol:
            return p
        
        # Paso 5
        i += 1

        # Paso 6
        p0 = p
    
    # Paso 7
    return print(f"El metodo falló despues de {n} iteraciones.")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def steffensen_descriptivo(gx,p0,tol,n):
    l0 = ["k","p0","p1","p2"]
    l1,l2,l3,l4 = [0],[p0],[],[]
    i = 1
    while i <= n:
        p1 = gx(p0)
        p2 = gx(p1)
        p = p0-(((p1-p0)**2)/(p2-(2*p1)+p0))
        l1.append(i)
        l2.append(p)
        l3.append(p1)
        l4.append(p2)
        if abs(p-p0) < tol:
            print(f"El método superó la representación (OverFlow) en {i} iteraciones.")
            return generate_dict(l0,l1,l2,l3,l4)
        i += 1
        p0 = p
    print(f"El método fracasó después de {i-1} iteraciones.")
    return generate_dict(l0,l1,l2,l3,l4)

print_ascii_table(steffensen_descriptivo(GX,P0,TOL,N_MAX))