import sympy as sp

def resolver_integral_doble(f, x_bounds, y_bounds):
    """
    Resuelve la integral doble de una función f(x, y) en el dominio definido por x_bounds y y_bounds.

    Args:
    f : sympy function
        La función a integrar.
    x_bounds : tuple
        Los límites de integración para x, en el formato (x_min, x_max).
    y_bounds : tuple
        Los límites de integración para y, en el formato (y_min, y_max).

    Returns:
    integral_result : sympy expression
        El resultado de la integral doble.
    """
    x, y = sp.symbols('x y')
    
    # Primera integración respecto a y
    inner_integral = sp.integrate(f, (y, y_bounds[0], y_bounds[1]))
    
    # Segunda integración respecto a x
    outer_integral = sp.integrate(inner_integral, (x, x_bounds[0], x_bounds[1]))
    
    return outer_integral
