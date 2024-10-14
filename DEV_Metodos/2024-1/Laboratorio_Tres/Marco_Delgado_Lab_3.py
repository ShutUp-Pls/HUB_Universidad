import numpy as np

'''
Actividad 1:
Implemente en Python el algoritmo de
la regla compuesta de Simpson para una integral doble.
'''
def simpson(a,b,m,n,d,c,f):
    # Paso 1
    h = (b-a)/n
    j1, j2, j3 = 0, 0, 0

    # Paso 2
    for i in range(0, n+1):

        # Paso 3
        x = a + (i*h)
        hx = (d(x)-c(x))/m
        k1 = f(x,c(x)) + f(x,d(x))
        k2, k3 = 0, 0

        # Paso 4
        for j in range(1, m):

            # Paso 5
            y = c(x) + j*hx
            q = f(x,y)

            # Paso 6
            if j%2 == 0: k2 += q
            else: k3 += q
        
        # Paso 7
        l = (k1 + 2*k2 + 4*k3)*(hx/3)

        # Paso 8
        if i == 0 or i == n: j1 += l
        elif i%2 == 0: j2 += l
        else: j3 += l
    
    # Paso 9
    j = (j1 + 2*j2 + 4*j3)* (h/3)

    # Paso 10
    return j

'''
Actividad 2:
Use el algoritmo de la regla compuesta de Simpson para una integral doble con n = m = 14 para
encontrar el centro de masa de la l ́amina descrita.
'''

# R = {(x,y)∈(R^2)/ 0 ≤ x ≤ 1, 0 ≤ y ≤ (e^x)}
#
# De la definicion de R se desprenden los valores de a, b, c(x) y d(x)
a = 0
b = 1
def c(x): return 0
def d(x): return np.exp(x)

# Definimos la densidad de la lamina dada por el problema
# o(x,y) = k (Constante)
# Usaremos un valor inocuo como placeholder
def o(x,y):
    k = 1.0
    return k

# Definimos el n y m dado por la actividad
n = 14
m = 14

# Definimos la funcion de la integral denominador en la division
# Calculamos y guardamos su valor
def f_denom(x,y): return o(x,y)
integral_denominador = simpson(a, b, m, n, d, c, f_denom)

# Definimos la funcion de la integral numerador en la division para x
# Calculamos y guardamos su valor
def f_num_x(x,y): return x*o(x,y)
integral_numerador_x = simpson(a, b, m, n, d, c, f_num_x)

# Definimos la funcion de la integral numerador en la division para y
# Calculamos y guardamos su valor
def f_num_y(x,y): return y*o(x,y)
integral_numerador_y = simpson(a, b, m, n, d, c, f_num_y)

# Calculamos el valor aproxumado del centro de masa de la lamina
x_aprox = integral_numerador_x/integral_denominador
y_aprox = integral_numerador_y/integral_denominador

print(f"El valor del centro de masa aproximado es:\n({x_aprox}, {y_aprox})\n")

'''
Actividad 3:
Usando el error relativo porcentual,
compare las aproximaciones obtenidas con el resultado exacto
'''

# Definimos el valor exacto del centro de masa
x = 1 / (np.e - 1)
y = (np.e + 1) / 4
print(f"Valor real del centro de masa:\n({x}, {y})\n")

# Calulamos el error relativo porcentual
error_rel_x = (abs(x-x_aprox)/abs(x))*100
error_rel_y = (abs(y-y_aprox)/abs(y))*100
print(f"El error de la aproximación para 'x' e 'y' respectivamete es:\n({error_rel_x}, {error_rel_y})\n")