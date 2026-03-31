import numpy as np

# Data dari soal
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])

# Bentuk matriks A (basis fungsi)
A = np.column_stack((
    np.log(x),      # ln(x)
    np.cos(x),      # cos(x)
    np.exp(x)       # e^x
))

# Least Squares Solution
coef, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

a, b, c = coef

print("Hasil fitting:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Prediksi
y_pred = A @ coef

print("\nPerbandingan data asli vs prediksi:")
for i in range(len(x)):
    print(f"x={x[i]:.2f}, y_asli={y[i]:.3f}, y_pred={y_pred[i]:.3f}")

# Error (Mean Squared Error)
mse = np.mean((y - y_pred)**2)
print("\nMSE =", mse)