import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Crear figura y ejes
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
plt.subplots_adjust(left=0.25, bottom=0.25)

# Inicialización de valores
t_min, t_max = 0, 2 * np.pi
r_min, r_max = 0, 1

# Datos iniciales
t = np.linspace(t_min, t_max, 500)
r_lower = r_min + (r_max - r_min) * np.sin(t)
r_upper = r_max + (r_min - r_max) * np.cos(t)

# Dibujar región inicial
region = ax.fill_between(t, r_lower, r_upper, color='blue', alpha=0.5)

# Configuración de los sliders
ax_t_min = plt.axes([0.25, 0.1, 0.65, 0.03])
ax_t_max = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_r_min = plt.axes([0.25, 0.2, 0.65, 0.03])
ax_r_max = plt.axes([0.25, 0.25, 0.65, 0.03])

slider_t_min = Slider(ax_t_min, 't Min', 0, 2 * np.pi, valinit=t_min)
slider_t_max = Slider(ax_t_max, 't Max', 0, 2 * np.pi, valinit=t_max)
slider_r_min = Slider(ax_r_min, 'r Min', 0, 1, valinit=r_min)
slider_r_max = Slider(ax_r_max, 'r Max', 0, 1, valinit=r_max)

# Función para actualizar la región
def actualizar(val):
    t_min = slider_t_min.val
    t_max = slider_t_max.val
    r_min = slider_r_min.val
    r_max = slider_r_max.val

    t = np.linspace(t_min, t_max, 500)
    # Puedes modificar estas funciones para r_lower y r_upper según desees
    r_lower = r_min + (r_max - r_min) * np.sin(t)
    r_upper = r_max + (r_min - r_max) * np.cos(t)
    
    ax.clear()  # Limpiar el gráfico
    ax.fill_between(t, r_lower, r_upper, color='blue', alpha=0.5)
    ax.set_title("Región en coordenadas polares")
    plt.draw()

# Conectar sliders con la función de actualización
slider_t_min.on_changed(actualizar)
slider_t_max.on_changed(actualizar)
slider_r_min.on_changed(actualizar)
slider_r_max.on_changed(actualizar)

# Mostrar la gráfica
plt.show()
