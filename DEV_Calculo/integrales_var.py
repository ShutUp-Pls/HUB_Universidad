import numpy as np
import matplotlib.pyplot as plt

def graficar_funciones(funciones_x_y, etiquetas_x_y, funciones_y_x, etiquetas_y_x, rango):
    """
    Grafica funciones dadas en listas separadas para x(y) y y(x), mostrando la leyenda en formato LaTeX.

    Args:
        funciones_x_y (list): Lista de funciones de la forma x(y).
        etiquetas_x_y (list): Lista de etiquetas LaTeX para funciones x(y).
        funciones_y_x (list): Lista de funciones de la forma y(x).
        etiquetas_y_x (list): Lista de etiquetas LaTeX para funciones y(x).
        rango (float): Rango para centrar la gráfica en (-rango, rango).
    """
    # Crear el espacio de gráficos
    fig, ax = plt.subplots(figsize=(8, 8))

    # Crear un rango para la variable independiente
    y_vals = np.linspace(-rango, rango, 500)
    x_vals = np.linspace(-rango, rango, 500)

    # Graficar funciones x(y)
    for f, etiqueta in zip(funciones_x_y, etiquetas_x_y):
        try:
            x = f(y_vals)
            ax.plot(x, y_vals, label=f"${etiqueta}$")
        except Exception as e:
            print(f"Error al graficar x(y): {e}")

    # Graficar funciones y(x)
    for f, etiqueta in zip(funciones_y_x, etiquetas_y_x):
        try:
            y = f(x_vals)
            ax.plot(x_vals, y, label=f"${etiqueta}$")
        except Exception as e:
            print(f"Error al graficar y(x): {e}")

    # Configuración del gráfico
    ax.set_xlim(-rango, rango)
    ax.set_ylim(-rango, rango)
    ax.axhline(0, color='black', linewidth=0.8, linestyle="--")
    ax.axvline(0, color='black', linewidth=0.8, linestyle="--")
    ax.set_aspect('equal', adjustable='box')
    ax.set_title("Gráfico de funciones")
    ax.legend()
    plt.grid()
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Definir funciones y sus etiquetas en LaTeX
    funciones_x_y = [lambda y: y**2, lambda y: np.sin(y)]
    etiquetas_x_y = ["x = y^2", "x = \\sin(y)"]

    funciones_y_x = [lambda x: np.sqrt(x), lambda x: np.cos(x)]
    etiquetas_y_x = ["y = \\sqrt{x}", "y = \\cos(x)"]

    # Ajustar rango de visualización
    rango = 5
    graficar_funciones(funciones_x_y, etiquetas_x_y, funciones_y_x, etiquetas_y_x, rango)
