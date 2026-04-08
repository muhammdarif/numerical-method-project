import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([0,1,2,3,4], dtype=float)
y = np.array([1,3,2,5,4], dtype=float)

# =============================
# 🔹 LAGRANGE
# =============================
def lagrange(x_data, y_data, x_target):
    n = len(x_data)
    result = 0
    
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x_target - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    
    return result


# =============================
# 🔹 NEWTON
# =============================
def newton_divided_diff(x_data, y_data):
    n = len(x_data)
    coef = np.copy(y_data).astype(float)
    
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x_data[j:n] - x_data[0:n-j])
    
    return coef

def newton_interpolation(x_data, coef, x_target):
    n = len(coef)
    result = coef[n-1]
    
    for k in range(n-2, -1, -1):
        result = result * (x_target - x_data[k]) + coef[k]
    
    return result


# =============================
# 🔹 HITUNG NILAI INTERPOLASI
# =============================
coef = newton_divided_diff(x, y)

# Range untuk grafik
x_range = np.linspace(min(x), max(x), 100)

y_lagrange = [lagrange(x, y, xi) for xi in x_range]
y_newton = [newton_interpolation(x, coef, xi) for xi in x_range]

# =============================
# 🔹 PLOT GRAFIK
# =============================
plt.figure()

# titik asli
plt.scatter(x, y, label="Data Asli")

# kurva
plt.plot(x_range, y_lagrange, label="Lagrange")
plt.plot(x_range, y_newton, linestyle='--', label="Newton")

plt.title("Interpolasi Newton vs Lagrange")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.show()