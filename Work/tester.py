from Work.Rational import Rational
from numpy import fabs, zeros


def dumb(a):
    n = len(a)
    x = [0]*(n)
    for i in range(n):
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1, n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i]/a[i][i]
    return x


def better(mat):
    a = zeros(shape=(len(mat), len(mat)))
    for i in range(len(mat)):
        col = zeros(len(mat))
        a[i] = col
    b = zeros(len(mat))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if j == len(mat[i]) - 1:
                b[i] = mat[i][j]
            else:
                a[i][j] = mat[i][j]

    n = len(b)
    x = zeros(n)
    for k in range(n-1):
        if fabs(a[k, k]) < 1.0e-12:
            for i in range(k+1, n):
                if fabs(a[i, k]) > fabs(a[k, k]):
                    a[[k, i]] = a[[i, k]]
                    b[[k, i]] = b[[i, k]]
                    break
        for i in range(k+1, n):
            if a[i, k] == 0:
                continue
            ratio = a[k, k]/a[i, k]
            for j in range(k, n):
                a[i, j] = a[k, j] - a[i, j]*ratio
            b[i] = b[k] - b[i]*ratio

    
    print("")
    for i in range(n): 
        for j in range(n): 
            print(a[i][j], end="   ")
        print("")

    for i in range(len(b)): 
        print(b[i])
    
    print("")


    x[n-1] = b[n-1] / a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for j in range(i+1, n):
            sum += a[i, j] * x[j]
        x[i] = (b[i] - sum) / a[i, i]
    return x


rows, cols = (3, 4)
mat = []
for i in range(rows):
    col = [0] * cols
    mat.append(col)
mat[0][0] = 3
mat[0][1] = 2
mat[0][2] = -5
mat[1][0] = 2
mat[1][1] = -3
mat[1][2] = 1
mat[2][0] = 1
mat[2][1] = 4
mat[2][2] = -1
mat[0][3] = 0
mat[1][3] = 0
mat[2][3] = 4
for i in range(len(mat)):
    print(mat[i])
x = dumb(mat)
print("Answer: ", x, "\n")
mat = [[2, 4, -2, -2, -4],
       [1, 2, 4, -3, 5],
       [-3, -3, 8, -2, 7],
       [-1, 1, 6, -3, 7]]
for i in range(len(mat)):
    print(mat[i])
x = better(mat)
print("Answer: ", x, "\n")
mat = [[3, 2, -1, 7],
       [5, 4, 2, 4],
       [-1, 1, -3, -1]]
for i in range(len(mat)):
    print(mat[i])
x = better(mat)
print("Answer: ", x, "\n")
mat = [[1, 3, 2, 1, -2],
       [4, 2, 1, 2, 2],
       [2, 1, 2, 3, 1],
       [1, 2, 4, 1, -1]]
for i in range(len(mat)):
    print(mat[i])
x = better(mat)
print("Answer: ", x, "\n")
mat = [[2, 4, -2, -2, -4],
       [1, 2, 4, -3, 5],
       [-3, -3, 8, -2, 7],
       [-1, 1, 6, -3, 7]]
x = better(mat)
for i in range(len(mat)):
    print(mat[i])
