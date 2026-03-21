import numpy as np

# Fungsi Jacobi
def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)

    for k in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # cek konvergensi
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Konvergen dalam {k+1} iterasi")
            return x_new

        x = x_new.copy()

    print("Tidak konvergen")
    return x

# Matriks A dan vektor b
A = np.array([
    [1, 8, -2],
    [-2, 4, -9],
    [10, -3, 6]
], dtype=float)

b = np.array([-9, -50, 24.5], dtype=float)

# Tebakan awal
x0 = np.zeros(3)

# Jalankan
hasil_jacobi = jacobi(A, b, x0)
print("Hasil Jacobi:", hasil_jacobi)