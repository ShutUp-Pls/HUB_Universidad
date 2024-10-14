import numpy as np

def diferencias_finitas(a, b, c, d, m, n, tol, max_i, f, g):
    # Paso 1
    h = (b-a)/n
    k = (d-c)/m

    x = np.zeros((n-1, 1))
    x = x.astype('float64')
    # Paso 2
    for i in range(1, n): x[i-1, 0] = a + (i*h)
    
    y = np.zeros((m-1, 1))
    y = y.astype('float64')

    # Paso 3
    for j in range(1, m): y[j-1, 0] = c + (j*k)

    # Paso 4
    w = np.zeros((n-1, m-1))
    w = w.astype('float64')

    # Paso 5
    lam = (h**2)/(k**2)
    u = 2*(1+lam)
    l = 1

    # Paso 6
    while l <= max_i:
        
        # Paso 7
        z = ((-h**2)*(f(x[0, 0], y[m-2, 0])) + g(a, y[m-2, 0]) + lam*g(x[0, 0], d) + lam*w[0, m-3] + w[1, m-2])/u
        norm = abs(z-w[0,m-2])
        w[0,m-2] = z

        # Paso 8
        for i in range(2, n-1):
            z = ((-h**2)*(f(x[i-1, 0], y[m-2, 0])) + lam*g(x[i-1, 0], d) + w[i-2, m-2] + w[i, m-2] + lam*w[i-1, m-3])/u
            if abs(w[i-1, m-2] - z) > norm: norm = abs(w[i-1, m-2] - z)
            w[i-1, m-2] = z

        # Paso 9
        z = ((-h**2)*f(x[n-2, 0], y[m-2, 0]) + g(b, y[m-2, 0]) + lam*g(x[n-2, 0], d) + w[n-3, m-2] + lam*w[n-2, m-3])/u
        if abs(w[n-2, m-2] - z) > norm: norm = abs(w[n-2, m-2] - z)
        w[n-2, m-2] = z

        # Paso 10
        for j in range(m-2, 1, -1):
            
            # Paso 11
            z = ((-h**2)*f(x[0, 0], y[j-1, 0]) + g(a, y[j-1, 0]) + lam*w[0, j] + lam*w[0, j-2] + w[1, j-1])/u
            if abs(w[0, j-1] - z) > norm: norm = abs(w[0, j-1] - z)
            w[0, j-1] = z

            # Paso 12
            for i in range(2, n-1):
                z = ((-h**2)*f(x[i-1, 0], y[j-1, 0]) + w[i-2, j-1] + lam*w[i-1, j] + w[i, j-1] + lam*w[i-1, j-2])/u
                if abs(w[i-1, j-1] - z) > norm: norm = abs(w[i-1, j-1] - z)
                w[i-1, j-1] = z
            
            # Paso 13
            z = ((-h**2)*f(x[n-2, 0], y[j-1, 0]) + g(b, y[j-1, 0]) + w[n-3, j-1] + lam*w[n-2, j] + lam*w[n-2, j-2])/u
            if abs(w[n-2, j-1] - z) > norm: norm = abs(w[n-2, j-1] - z)
            w[n-2, j-1] = z
        
        # Paso 14
        z = ((-h**2)*f(x[0,0], y[0,0]) + g(a, y[0, 0]) + lam*g(x[0, 0], c) + lam*w[0,1] + w[1,0])/u
        if abs(w[0,0] - z) > norm: norm = abs(w[0,0] - z)
        w[0,0] = z

        # Paso 15
        for i in range(2, n-1):
            z = ((-h**2)*f(x[i-1, 0], y[0, 0]) + lam*g(x[i-1, 0], c) + w[i-2, 0] + lam*w[i-1, 1] + w[i, 0])/u
            if abs(w[i-1, 0] - z) > norm: norm = abs(w[i-1, 0] - z)
            w[i-1, 0] = z

        # Paso 16
        z = ((-h**2)*f(x[n-2, 0], y[0, 0]) + g(b, y[0, 0]) + lam*g(x[n-2, 0], c) + w[n-3, 0] + lam*w[n-2, 1])/u
        if abs(w[n-2, 0] - z) > norm: norm = abs(w[n-2, 0] - z)
        w[n-2, 0] = z

        # Paso 17
        if norm <= tol:
            resultado = []
            # Paso 18
            for i in range(1, n):
                for j in range(1, m):
                    resultado.append((x[i-1, 0], y[j-1, 0], w[i-1, j-1]))
            
            # Paso 19
            return l, resultado
        
        # Paso 20
        l += 1
    
    #Paso 21
    return print("Se excedió el numero máximo de iteraciones.")


# Ejemplo 2 del burden (Pag 713)
N = 6
M = 5

def f(x,y): return x*(np.e**y)
def g(x,y): return x*(np.e**y)

iteracion, resultados = diferencias_finitas(0,2,0,1,M,N,1e-10,100, f, g)

if resultados:
    for res in resultados:
        print(f"({res[0]}, {res[1]}, {res[2]})")
    print(f"Resuelto en {iteracion} iteraciones")
