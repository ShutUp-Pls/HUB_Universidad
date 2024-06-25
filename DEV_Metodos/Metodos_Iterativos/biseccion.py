import ecuaciones as ec

from ASCII_Tabla import print_ascii_table, generate_dict

FX = ec.f1
A_I = ec.A_F1
B_I = ec.B_F1
TOL = 0
N_MAX = 13

# Metodo 1:1 a las indicaciones del BURDEN
def metodo_biseccion(f, a, b, tol, n):
    
    # Paso 1
    i = 1
    fa = f(a)

    # Paso 2
    while i <= n:

        # Paso 3
        p = a+((b-a)/2)
        fp = f(p)

        # Paso 4
        if (fp == 0) or ((b-a)/2 < tol):
            return p
        
        # Paso 5
        i += 1

        # Paso 6
        if (fa*fp > 0):
            a = p
            fa = fp
        else:
            b = p
    
    # Paso 7
    return print(f"El metodo fracasó después de {n} iteraciones")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def metodo_biseccion_descriptivo(f, a, b, tol, n):
    l0 = ["n", "a", "b", "p", "f(p)"]
    l1,l2,l3,l4,l5 = [],[],[],[],[]

    i = 1
    fa = f(a)

    while i <= n:
        p = a+((b-a)/2)
        fp = f(p)

        l1.append(i)
        l2.append(a)
        l3.append(b)
        l4.append(p)
        l5.append(fp)

        if fp == 0:
            print(f"FeedBack: El metodo encontró la raiz luego de {n} iteraciones")
            return generate_dict(l0,l1,l2,l3,l4,l5)
        
        elif (b-a)/2 < tol:
            print(f"FeedBack: El metodo superó la tolerancia luego de {n} iteraciones")
            return generate_dict(l0,l1,l2,l3,l4,l5)
        
        i += 1
        if (fa*fp > 0):
            a = p
            fa = fp
        else:
            b = p

    print(f"FeedBack: El metodo fracasó después de {n} iteraciones")
    return generate_dict(l0,l1,l2,l3,l4,l5)

def main():
    print_ascii_table(
        metodo_biseccion_descriptivo(FX,A_I,B_I,TOL,N_MAX)
    )