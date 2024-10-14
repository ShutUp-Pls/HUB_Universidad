import ecuaciones as ec

from ASCII_Tabla import print_ascii_table, generate_dict, add_last_elements

G1 = ec.g1
G2 = ec.g2
G3 = ec.g3
G4 = ec.g4
G5 = ec.g5
P0 = ec.P0_F1

TOL = 1e-13
N_MAX = 100

# Metodo 1:1 a las indicaciones del BURDEN
def punto_fijo(g, p0, tol, n):

    # Paso 1
    i = 1

    # Paso 2
    while i <= n:

        # Paso 3
        p = g(p0)

        # Paso 4
        if abs(p-p0) < tol:
            return p
        
        # Paso 4
        i += 1

        # Paso 6
        p0 = p

    # Paso 7
    return print(f"El método fracasó después de {n} iteraciones.")

# Metodo retorna diccionarios para crear tablas a traves de la funcion ASCII
def punto_fijo_descriptivo(g, p0, tol, n):
    l0 = [f"n",f"p"]
    l1,l2 = [],[]
    overflow_limite = 1e10

    i = 0
    while i <= n:
        p = g(p0)

        l1.append(i)
        l2.append(p0)

        if abs(p) > overflow_limite:
            print(f"El método superó la representación (OverFlow) en {i} iteraciones.")
            return generate_dict(l0,l1,l2)

        if abs(p-p0) < tol:
            print(f"El método superó la tolerancia después de {i} iteraciones.")
            return generate_dict(l0,l1,l2)
        
        i += 1
        p0 = p
    print(f"El método fracasó después de {i-1} iteraciones.")
    return generate_dict(l0,l1,l2)

dict_g1 = punto_fijo_descriptivo(G1,P0,TOL,N_MAX)
dict_g2 = punto_fijo_descriptivo(G2,P0,TOL,N_MAX)
dict_g3 = punto_fijo_descriptivo(G3,P0,TOL,N_MAX)
dict_g4 = punto_fijo_descriptivo(G4,P0,TOL,N_MAX)
dict_g5 = punto_fijo_descriptivo(G5,P0,TOL,N_MAX)

print_ascii_table(add_last_elements(dict_g1,dict_g2,dict_g3,dict_g4,dict_g5))