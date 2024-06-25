import sympy as sp

# Definir las variables

# Parametro
a = sp.symbols('a')
 # Variables
x, y = sp.symbols('x y')

# Funciones y Limites de integracion
F1 = a-x-y
F1_XL = (0, a)
F1_YL = (0, a)

F2 = (2*x)-y
F2_XL = (0, 2)
F2_YL = (0, 1)
