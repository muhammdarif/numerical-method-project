import matplotlib.pyplot as plt


# Fungsi
def f(x):
    return x**3 - x - 2

def secant(f, x0, x1, tol=1e-6, max_iter=100):

    errors = []

    print("Metode Secant")
    print("---------------------------------------------------")
    print("Iter |    x(i-1)    x(i)      Error")
    print("---------------------------------------------------")

    for i in range(1, max_iter+1):

        if (f(x1) - f(x0)) == 0:
            print("Pembagi nol! Metode gagal.")
            return None

        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        error = abs(x2 - x1)
        errors.append(error)

        print(f"{i:3d} | {x0:.6f}   {x1:.6f}   {error:.6f}")

        if error < tol:
            print("---------------------------------------------------")
            print("Akar ditemukan:", x2)
            print("Jumlah iterasi:", i)
            break

        x0 = x1
        x1 = x2

    # 📊 Grafik Konvergensi
    plt.figure()
    plt.plot(range(1, len(errors)+1), errors)
    plt.title("Grafik Konvergensi Metode Secant")
    plt.xlabel("Iterasi")
    plt.ylabel("Error")
    plt.show()


# PEMANGGILAN PROGRAM
secant(f, 1, 2)
