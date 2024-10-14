import numpy as np

def lu_dolittle_crout(A):
    n = len(A)
    L = np.eye(n)  # Inicializamos L como una matriz identidad
    U = np.zeros((n, n))  # Inicializamos U como una matriz de ceros

    # Factorización LU en forma de Dolittle
    for k in range(n):
        U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
        L[(k+1):, k] = (A[(k+1):, k] - L[(k+1):, :] @ U[:, k]) / U[k, k]

    L_dolittle = L
    U_dolittle = U

    # Factorización LU en forma de Crout
    L = np.zeros((n, n))  # Reiniciamos L como matriz de ceros
    U = np.eye(n)  # Reiniciamos U como matriz identidad

    for k in range(n):
        L[k:, k] = A[k:, k] - L[k:, :] @ U[:, k]
        U[k, (k+1):] = (A[k, (k+1):] - L[k, :] @ U[:, (k+1):]) / L[k, k]

    L_crout = L
    U_crout = U

    return L_dolittle, U_dolittle, L_crout, U_crout

# Ejemplo de uso:
A = np.array([[16, 8, 4],
              [8, 29, 17],
              [6, 17, 26]])

L_dolittle, U_dolittle, L_crout, U_crout = lu_dolittle_crout(A)

print("Factorización LU en forma de Dolittle:")
print("L_dolittle:")
print(L_dolittle)
print("U_dolittle:")
print(U_dolittle)

print("\nFactorización LU en forma de Crout:")
print("L_crout:")
print(L_crout)
print("U_crout:")
print(U_crout)
