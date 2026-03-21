import numpy as np

# Fungsi Gauss-Seidel
def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))       # pakai nilai baru
            s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))  # nilai lama
            x[i] = (b[i] - s1 - s2) / A[i][i]

        # cek konvergensi
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            print(f"Konvergen dalam {k+1} iterasi")
            return x

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
hasil_gs = gauss_seidel(A, b, x0)
print("Hasil Gauss-Seidel:", hasil_gs)