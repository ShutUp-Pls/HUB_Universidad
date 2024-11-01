import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return 2*(x**3) + x + 1   # Raíces en x = -sqrt(3), 0 y sqrt(3)

# Rango de valores x ajustado
x = np.linspace(-2, 1, 400)
y = funcion(x)

# Graficar
plt.figure(figsize=(10, 6))

# Graficar la función completa
plt.plot(x, y, label=r'$f(x) = 2x^3+x+1$', color='blue')  # Color original

# Valores de f en -1 y 0
f1 = funcion(-1)
f2 = funcion(0)

# Resaltar el intervalo [-1, 0] en rojo
x_resaltado = np.linspace(-1, 0, 200)  # Intervalo a resaltar
y_resaltado = funcion(x_resaltado)
plt.plot(x_resaltado, y_resaltado, color='red', linewidth=2, label='Intervalo [a, b]')  # Color resaltado

# Añadir barras en los bordes del intervalo, limitando la altura
plt.plot([-1, -1], [f1-1, f1+1], color='red', linestyle='-', linewidth=2)  # Línea en x = -1
plt.text(-1, f1+1.4, r'$a$', fontsize=16, color='red', ha='center')  # Etiqueta para a = -1

plt.plot([0, 0], [f2-1, f2+1], color='red', linestyle='-', linewidth=2)  # Línea en x = 0
plt.text(0, f2+1.4, r'$b$', fontsize=16, color='red', ha='center')  # Etiqueta para b = 0

# Calcular y graficar el punto medio
a = -1
b = 0
punto_medio = (a + b) / 2
f_medio = funcion(punto_medio)

# Graficar el punto medio
plt.plot(punto_medio, f_medio, 'o', color='orange', markersize=8, label='Punto Medio')  # Punto medio en naranja
plt.text(punto_medio, f_medio + 1, r'$\frac{a+b}{2}$', fontsize=12, color='orange', ha='center')  # Etiqueta para el punto medio

plt.axhline(0, color='black', lw=0.5, ls='--')  # Línea horizontal en y=0
plt.axvline(0, color='black', lw=0.5, ls='--')  # Línea vertical en x=0
plt.title('Método de Bisección')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.ylim(-10, 10)  # La extensión en y se mantiene
plt.xlim(-2, 1)  # Mantener el límite en el eje x
plt.show()
