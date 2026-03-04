import math
def f(x):
    return x - math.cos(x)

def df(x):
    return 1 + math.sin(x)

def newton(x0, tol=1e-15, max_iter=20):

    print("Newton Method untuk f(x)=x-cos(x)")
    print("------------------------------------------------")

    x = x0
    for i in range(1, max_iter+1):
        print(f"Iterasi {i}: {x:.15f}")
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            break
        x = x_new
newton(0.6)
