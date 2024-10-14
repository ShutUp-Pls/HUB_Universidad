import numpy as np

def sumatoria(expresion, a, b):
    suma = 0
    for k in range(a,b):
        suma += expresion

B = np.array([[2,3,4],
              [4,5,6],
              [6,7,8]])

print(B[1,1])
#sumatoria(B)