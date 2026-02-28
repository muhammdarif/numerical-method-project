import matplotlib.pyplot as plt


def f(x):
    return x**3 - x - 2

def bisection(f, a, b, tol=1e-6, max_iter=100):

    errors = []
    c_old = a

    print("Metode Bisection")
    print("---------------------------------------------------")
    print("Iter |     c        f(c)        Error")
    print("---------------------------------------------------")

    for i in range(1, max_iter+1):
        c = (a+b)/2
        fc = f(c)
        error = abs(c - c_old)
        errors.append(error)

        print(f"{i:3d} | {c:.6f}   {fc:.6f}   {error:.6f}")

        if fc == 0 or error < tol:
            print("---------------------------------------------------")
            print("Akar ditemukan:", c)
            print("Jumlah iterasi:", i)
            break

        if f(a)*fc < 0:
            b = c
        else:
            a = c

        c_old = c

    # 📊 Grafik Konvergensi
    plt.figure()
    plt.plot(range(1, len(errors)+1), errors)
    plt.title("Grafik Konvergensi Metode Bisection")
    plt.xlabel("Iterasi")
    plt.ylabel("Error")
    plt.show()


bisection(f, 1, 2)
