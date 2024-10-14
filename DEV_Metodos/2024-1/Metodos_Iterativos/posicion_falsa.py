from ASCII_Tabla import generate_dict, print_ascii_table

import ecuaciones as ec

FX = ec.f2
P0 = ec.P0_F2
P1 = ec.P1_F2

TOL = 1e-8
N_MAX = 100

# Metodo 1:1 a las indicaciones del BURDEN
def posicion_falsa(fx,p0,p1,tol,n):
    
    # Paso 1
    i = 2
    q0 = fx(p0)
    q1 = fx(p1)

    # Paso 2
    while i <= n:

        # Paso 3
        p = p1-((q1*(p1-p0))/(q1-q0))

        # Paso 4
        if abs(p-p1) < tol:
            return p
        
        # Paso 5
        i += 1
        q = fx(p)

        # Paso 6
        if (q*q1) < 0:
            p0 = p1
            q0 = q1

        # Paso 7
        p1 = p
        q1 = q

    # Paso 8
    return print(f"El metodo falló después de {n}")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def posicion_falsa_descriptivo(fx,p0,p1,tol,n):
    l0 = ["n","p"]
    l1,l2 = [0,1],[p0,p1]
    i = 2
    q0 = fx(p0)
    q1 = fx(p1)
    while i <= n:
        p = p1-((q1*(p1-p0))/(q1-q0))
        l1.append(i)
        l2.append(p)
        if abs(p-p1) < tol:
            print(f"El metodo supera la tolerancia despues de {i} iteraciones.")
            return generate_dict(l0,l1,l2)
        i += 1
        q = fx(p)
        if (q*q1) < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print(f"El metodo falla despues de {i-1} iteraciones.")
    return generate_dict(l0,l1,l2)

print_ascii_table(posicion_falsa_descriptivo(FX,P0,P1,TOL,N_MAX))