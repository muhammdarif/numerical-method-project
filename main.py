import matplotlib.pyplot as plt


# Fungsi
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1


# ================= BISECTION =================
def bisection_errors(f, a, b, tol=1e-6, max_iter=100):
    errors = []
    c_old = a

    for i in range(max_iter):
        c = (a+b)/2
        error = abs(c - c_old)
        errors.append(error)

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

        if error < tol:
            break

        c_old = c

    return errors


# ================= NEWTON =================
def newton_errors(f, df, x0, tol=1e-6, max_iter=100):
    errors = []

    for i in range(max_iter):
        x1 = x0 - f(x0)/df(x0)
        error = abs(x1-x0)
        errors.append(error)

        if error < tol:
            break

        x0 = x1

    return errors


# ================= SECANT =================
def secant_errors(f, x0, x1, tol=1e-6, max_iter=100):
    errors = []

    for i in range(max_iter):
        x2 = x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        error = abs(x2-x1)
        errors.append(error)

        if error < tol:
            break

        x0=x1
        x1=x2

    return errors


# Ambil Data Error
err_bis = bisection_errors(f,1,2)
err_new = newton_errors(f,df,1.5)
err_sec = secant_errors(f,1,2)


# ================= PLOT GABUNGAN =================
plt.figure()

plt.plot(range(1,len(err_bis)+1), err_bis)
plt.plot(range(1,len(err_new)+1), err_new)
plt.plot(range(1,len(err_sec)+1), err_sec)

plt.title("Perbandingan Konvergensi Metode Numerik")
plt.xlabel("Iterasi")
plt.ylabel("Error")

plt.legend(["Bisection","Newton","Secant"])

plt.show()
