import numpy as np

A = np.array([
[1,1,1,0,0,0],
[0,-1,0,1,-1,0],
[0,0,-1,0,0,1],
[0,0,0,0,1,-1],
[0,12,-12,0,-18,-7],
[7,-12,0,-25,0,0]
], dtype=float)

B = np.array([0,0,0,0,0,150], dtype=float)

n = len(B)

M = np.hstack((A,B.reshape(-1,1)))

for i in range(n):
    for j in range(i+1,n):
        ratio = M[j][i]/M[i][i]
        for k in range(n+1):
            M[j][k] -= ratio*M[i][k]

x = np.zeros(n)

for i in range(n-1,-1,-1):
    x[i] = M[i][n]
    for j in range(i+1,n):
        x[i] -= M[i][j]*x[j]
    x[i] /= M[i][i]

print("i12 =",x[0])
print("i52 =",x[1])
print("i32 =",x[2])
print("i65 =",x[3])
print("i54 =",x[4])
print("i43 =",x[5])
