def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

def newton_raphson(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x)/df(x)
        
        print(f"Iterasi {i+1}: x = {x_new}")

        if abs(x_new - x) < tol:
            print("\nAkar ditemukan:", x_new)
            return x_new
        
        x = x_new
    
    print("\nMetode tidak konvergen")
    return None

# Parameter
x0 = 1.5
tol = 0.0001
max_iter = 20

newton_raphson(x0, tol, max_iter)
