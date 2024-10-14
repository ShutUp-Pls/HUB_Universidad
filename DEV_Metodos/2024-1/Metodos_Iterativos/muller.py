from ASCII_Tabla import generate_dict, print_ascii_table

import ecuaciones as ec

FX = ec.f3
X0 = ec.P0_X0
X1 = ec.P0_X1
X2 = ec.P0_X2

TOL = 1e-5
N_MAX = 100

# Metodo 1:1 a las indicaciones del BURDEN
def muller(fx,x0,x1,x2,tol,n):

    # Paso 1
    h1 = x1-x0
    h2 = x2-x1
    o1 = (fx(x1)-fx(x0))/h1
    o2 = (fx(x2)-fx(x1))/h2
    d = (o2-o1)/(h2+h1)
    i = 3

    # Paso 2
    while i <= n:

        # Paso 3
        b = o2+(h2*d)
        dm = ((b**2)-(4*fx(x2)*d))**(1/2)

        # Paso 4
        if abs(b-dm) < abs(b+dm):
            em = b+dm
        else:
            em = b-dm

        # Paso 5
        h = (-2*fx(x2))/em
        p = x2 + h

        # Paso 6
        if abs(h) < tol:
            return p
        
        # Paso 7
        x0 = x1
        x1 = x2
        x2 = p
        h1 = (x1-x0)
        h2 = (x2-x1)
        o1 = (fx(x1)-fx(x0))/h1
        o2 = (fx(x2)-fx(x1))/h2
        d = (o2-o1)/(h2+h1)
        i += 1

    # Paso 8
    return print(f"El metodo falló después de {n} iteraciones")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def muller_descriptivo(fx,x0,x1,x2,tol,n):
    l0 = ["i","x","fx"]
    l1,l2,l3 = [],[],[]
    h1 = x1-x0
    h2 = x2-x1
    o1 = (fx(x1)-fx(x0))/h1
    o2 = (fx(x2)-fx(x1))/h2
    d = (o2-o1)/(h2+h1)
    i = 3
    while i <= n:
        b = o2+(h2*d)
        dm = ((b**2)-(4*fx(x2)*d))**(1/2)
        if abs(b-dm) < abs(b+dm):
            em = b+dm
        else:
            em = b-dm
        h = (-2*fx(x2))/em
        p = x2 + h
        l1.append(i)
        l2.append(p)
        l3.append(fx(p))
        if abs(h) < tol:
            print(f"El metodo supera la tolerancia despues de {i} iteraciones.")
            return generate_dict(l0,l1,l2,l3)
        x0 = x1
        x1 = x2
        x2 = p
        h1 = (x1-x0)
        h2 = (x2-x1)
        o1 = (fx(x1)-fx(x0))/h1
        o2 = (fx(x2)-fx(x1))/h2
        d = (o2-o1)/(h2+h1)
        i += 1
    print(f"El metodo falla despues de {i-1} iteraciones.")
    return generate_dict(l0,l1,l2,l3)

print_ascii_table(muller_descriptivo(FX,X0,X1,X2,TOL,N_MAX))