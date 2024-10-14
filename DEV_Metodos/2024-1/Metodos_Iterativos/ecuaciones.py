from math import cos, pi

def f1(x): return (x**3)+(4*(x**2))-10
def f2(x): return cos(x)-x
def f3(x): return (16*(x**4))-(40*(x**3))+(5*(x**2))+(20*x)+6

# Intervalo [A_F,B_F]
A_F1 = 1.0
B_F1 = 2.0

# Puntos Fijo
P0_F1 = 1.5

P0_F2 = 0.5
P1_F2 = pi/4

P0_X0 = 0.5
P0_X1 = -0.5
P0_X2 = 0

P1_X0 = 0.5
P1_X1 = 1.0
P1_X2 = 1.5

P2_X0 = 2.5
P2_X1 = 2.0
P2_X2 = 2.25

# Desde g1 hasta g5 son f1 de la forma x=f1 en vez de f1=0
# Utiles para probar punto fijo (Ejemplos del BURDEN)
def g1(x): return x-(x**3)-(4*(x**2))+10
def g2(x): return ((10/x)-(4*x))**(1/2)
def g3(x): return (1/2)*((10-(x**3))**(1/2))
def g4(x): return (10/(4+x))**(1/2)
def g5(x): return x-(((x**3)+(4*(x**2))-10)/((3*(x**2))+(8*x)))