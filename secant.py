import math
def f(x):
    return x - math.cos(x)

def secant(x0, x1, tol=1e-15, max_iter=20):

    print("Secant Method untuk f(x)=x-cos(x)")
    print("------------------------------------------------")

    print(f"Iterasi 1: {x0:.15f}")
    print(f"Iterasi 2: {x1:.15f}")

    for i in range(3, max_iter+1):

        if f(x1) - f(x0) == 0:
            print("Pembagi nol, metode berhenti")
            return

        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))

        print(f"Iterasi {i}: {x2:.15f}")

        if abs(x2 - x1) < tol:
            break

        x0, x1 = x1, x2
secant(0.6, 0.8)
