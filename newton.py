import matplotlib.pyplot as plt


# Fungsi
def f(x):
    return x**3 - x - 2

# Turunan fungsi
def df(x):
    return 3*x**2 - 1

def newton(f, df, x0, tol=1e-6, max_iter=100):

    errors = []

    print("Metode Newton-Raphson")
    print("---------------------------------------------------")
    print("Iter |    x(i)      f(x)        Error")
    print("---------------------------------------------------")

    for i in range(1, max_iter+1):

        if df(x0) == 0:
            print("Turunan nol! Metode gagal.")
            return None

        x1 = x0 - f(x0)/df(x0)
        error = abs(x1 - x0)
        errors.append(error)

        print(f"{i:3d} | {x0:.6f}   {f(x0):.6f}   {error:.6f}")

        if error < tol:
            print("---------------------------------------------------")
            print("Akar ditemukan:", x1)
            print("Jumlah iterasi:", i)
            break

        x0 = x1

    # 📊 Grafik Konvergensi
    plt.figure()
    plt.plot(range(1, len(errors)+1), errors)
    plt.title("Grafik Konvergensi Metode Newton-Raphson")
    plt.xlabel("Iterasi")
    plt.ylabel("Error")
    plt.show()


# PEMANGGILAN PROGRAM
newton(f, df, 1.5)
