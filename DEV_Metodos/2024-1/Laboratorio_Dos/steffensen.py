from ASCII_Tabla import generate_dict, print_ascii_table

'''
# ACTIVIDADES:
'''

# Valores Dados
V = 1e6
Q = 1e5
W = 1e6
K = 0.25

'''
# (1) Escriba la ecuación (0.1) en la forma c = g(c).
'''
GC = lambda c: (W-(K*V*(c**(1/2))))/Q

'''
# (2) Implemente en Python el algoritmo del método de Steffensen.
# Metodo con implementación grafica
'''
def steffensen_descriptivo(gx,p0,tol,n,graf=False):
    # Listas Necesarias para Implementación grafica ASCII
    l0 = ["k","p0","p1","p2"]
    l1,l2,l3,l4 = [0],[p0],[],[]

    # Paso 1
    i = 1
    # Paso 2
    while i <= n:
        # Paso 3
        p1 = gx(p0)
        p2 = gx(p1)
        p = p0-(((p1-p0)**2)/(p2-(2*p1)+p0))

        # Se añade a las listas los datos de interes
        # para la representación grafica completa
        l1.append(i)
        l2.append(p)
        l3.append(p1)
        l4.append(p2)

        # Paso 4
        if abs(p-p0) < tol:
            print(f"El método superó la tolerancia en {i} iteraciones.\n Raíz encontrada: {p}")
            if graf: return print_ascii_table(generate_dict(l0,l1,l2,l3,l4))
            else: return p
        # Paso 5
        i += 1
        # Paso 6
        p0 = p

    # Paso 7
    print(f"El método fracasó después de {i-1} iteraciones.\n Último valor encontrado: {p}")
    if graf: return print_ascii_table(generate_dict(l0,l1,l2,l3,l4))
    else: return -1

'''
# (3) Encuentre el punto fijo de la función g del ítem (1):
# (a) Graficamente
'''
# Se agregó una ScreenShot de GeoGebra al directorio
# para encontrar el valor de forma grafica

'''
# (b) Empleando el algoritmo del método de Steffensen
# considerando una tolerancia del 10^-10 y un maximo de 100 iteraciones
'''
# Se define tolerancia e iteraciones maximas
TOL = 1e-10
N_MAX = 100

# Punto para empezar a iterar
P0 = 1.0

# Implementación del metodo
steffensen_descriptivo(GC,P0,TOL,N_MAX,True)