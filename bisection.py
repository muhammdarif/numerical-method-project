import math
def f(x):
    return x - math.cos(x)

def bisection(a, b, tol=1e-15, max_iter=20):

    if f(a)*f(b) > 0:
        print("Interval tidak valid")
        return
    
    print("Bisection Method untuk f(x)=x-cos(x)")
    print("------------------------------------------------")

    for i in range(1, max_iter+1):
        c = (a + b) / 2
        
        print(f"Iterasi {i}: {c:.15f}")

        if abs(f(c)) < tol:
            break

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
bisection(0.6, 0.8)
