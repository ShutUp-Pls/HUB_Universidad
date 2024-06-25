import integrales_var as iv

from integral_doble_func import resolver_integral_doble

# Resolver la integral doble
resultado = resolver_integral_doble(iv.F2, iv.F2_XL, iv.F2_YL)
print(f"El resultado de la integral doble es: {resultado}")