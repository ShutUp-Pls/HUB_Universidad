import sympy as sp

def check_limit(func, variables, point):
    """
    Verifica la existencia del límite de una función en varias variables.

    Parameters:
    func (sympy function): La función a evaluar.
    variables (list): Lista de variables (ej: [x, y]).
    point (list): El punto al que se aproxima el límite (ej: [a, b]).

    Returns:
    dict: Un diccionario con la existencia del límite y su valor.
    """

    # Definir las variables
    var_symbols = sp.symbols(variables)
    point_dict = {var_symbols[i]: point[i] for i in range(len(point))}
    
    # Convertir la función al punto de interés
    func_at_point = func.subs(point_dict)
    
    # Verificar límite en diferentes caminos
    limit_exists = True
    limit_value = None
    paths = [
        (var_symbols[0], point[0], 0),  # Línea vertical (x=a)
        (var_symbols[1], point[1], 0),  # Línea horizontal (y=b)
        (var_symbols[0], point[0], var_symbols[0] - point[0] + point[1]),  # Línea y = x
        (var_symbols[0], point[0], (var_symbols[0] - point[0])**2 + point[1])  # Curva y = (x-a)^2 + b
    ]

    for var, p, expr in paths:
        substituted_func = func.subs({var: expr}).subs(var_symbols[0], var)
        limit_path = sp.limit(substituted_func, var, p)

        if limit_value is None:
            limit_value = limit_path
        elif limit_value != limit_path:
            limit_exists = False
            break

    # Verificar límite en coordenadas polares
    r, theta = sp.symbols('r theta')
    polar_func = func.subs({var_symbols[0]: point[0] + r * sp.cos(theta), var_symbols[1]: point[1] + r * sp.sin(theta)})
    limit_polar = sp.limit(polar_func, r, 0)

    if limit_exists and limit_value != limit_polar:
        limit_exists = False

    return {"limit_exists": limit_exists, "limit_value": limit_value if limit_exists else None}

# Ejemplo de uso
x, y = sp.symbols('x y')
func = sp.sin(x**2 + y**2) / (x**2 + y**2)
variables = ['x', 'y']
point = [0, 0]

result = check_limit(func, variables, point)
print(f"El límite existe: {result['limit_exists']}")
if result['limit_exists']:
    print(f"Valor del límite: {result['limit_value']}")
else:
    print("El límite no existe.")
