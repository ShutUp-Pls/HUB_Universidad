import numpy as np

# Ejemplo de matriz
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [17, 18, 19],
              [71, 81, 91]])

# Índices de las filas que deseas intercambiar
i, j = 0, 3  # Intercambiar la fila 0 con la fila 2

# Intercambio de filas en una sola línea
a[[i, j]] = a[[j, i]]

print(a)
