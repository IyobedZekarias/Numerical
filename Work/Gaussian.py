from Work.Rational import Rational

def dumb(a): 
    n = len(a)
    x = [0]*(n)

    for i in range(n):
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i]/a[i][i]

    return x


def better(mat): 
    a = []
    for i in range(len(mat)): 
        col = [Rational(0,1)] * len(mat)
        a.append(col)
    b = [Rational(0,1)] * len(mat)
    for i in range(len(mat)): 
        for j in range(len(mat[i])): 
            if j == len(mat[i]) - 1: 
                b[i] = mat[i][j]
            else: 
                a[i][j] = mat[i][j]
    
    n = len(b)
    x = [Rational(0,1)] * n

    for k in range(n-1):
        if abs(a[k][k]) < Rational(1, 1.0e12):
            
            for i in range(k+1, n):
                if abs(a[i][k]) > abs(a[k][k]):
                    temp = a[k]
                    a[k] = a[i]
                    a[i] = temp
                    temp = b[k]
                    b[k] = b[i]
                    b[i] = temp
                    break

        for i in range(k+1,n):
            if a[i][k] == Rational(0, 1): continue
            ratio = a[k][k]/a[i][k]
            for j in range(k,n):
                a[i][j] = a[k][j] - a[i][j]*ratio
            b[i] = b[k] - b[i]*ratio


    # print("")
    # for i in range(n): 
    #     for j in range(n): 
    #         print(a[i][j], end="   ")
    #     print("")

    # for i in range(len(b)): 
    #     print(b[i])
    
    # print("")


    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = Rational(0, 1)
        for j in range(i+1, n):
            sum += a[i][j] * x[j]
        x[i] = (b[i] - sum) / a[i][i]

    return x
    




# rows, cols = (3, 4)
# mat = []
# for i in range(rows): 
#     col = [0] * cols
#     mat.append(col)
# mat[0][0] = Rational(3, 1)
# mat[0][1] = Rational(2, 1)
# mat[0][2] = Rational(-5, 1)
# mat[1][0] = Rational(2, 1)
# mat[1][1] = Rational(-3, 1)
# mat[1][2] = Rational(1, 1)
# mat[2][0] = Rational(1, 1)
# mat[2][1] = Rational(4, 1)
# mat[2][2] = Rational(-1, 1)
# mat[0][3] = Rational(0, 1)
# mat[1][3] = Rational(0, 1)
# mat[2][3] = Rational(4, 1)
# for i in range(len(mat)): 
#     for j in range(len(mat[i])):
#         print(mat[i][j], end="    "),
#     print("")

# x = dumb(mat)
# print("\nAnswer: ")
# for i in range(len(x)): 
#     print(x[i], end="   " ) 
# print("\n")


# mat = [[Rational(2, 1), Rational(4, 1), Rational(-2, 1), Rational(-2, 1), Rational(-4, 1)], 
#        [Rational(1, 1), Rational(2, 1), Rational(4, 1), Rational(-3, 1), Rational(5, 1)], 
#        [Rational(-3, 1), Rational(-3, 1), Rational(8, 1), Rational(-2, 1), Rational(7, 1)], 
#        [Rational(-1, 1), Rational(1, 1), Rational(6, 1), Rational(-3, 1), Rational(7, 1)]]

# for i in range(len(mat)): 
#     for j in range(len(mat[i])):
#         print(mat[i][j], end="    "),
#     print("")

# x = better(mat)
# print("\nAnswer: ")
# for i in range(len(x)): 
#     print(x[i], end="   " ) 
# print("\n")


# mat = [[Rational(3, 1), Rational(2, 1), Rational(-1, 1), Rational(7, 1)],
#        [Rational(5, 1), Rational(3, 1), Rational(2, 1), Rational(4, 1)], 
#        [Rational(-1, 1), Rational(1, 1), Rational(-3, 1), Rational(-1, 1)]]

# for i in range(len(mat)): 
#     for j in range(len(mat[i])):
#         print(mat[i][j], end="    "),
#     print("")

# x = better(mat)
# print("\nAnswer: ")
# for i in range(len(x)): 
#     print(x[i], end="   " ) 
# print("\n")

# mat = [[Rational(1, 1), Rational(3, 1), Rational(2, 1), Rational(1, 1), Rational(-2, 1)], 
#        [Rational(4, 1), Rational(2, 1), Rational(1, 1), Rational(2, 1), Rational(2, 1)], 
#        [Rational(2, 1), Rational(1, 1), Rational(2, 1), Rational(3, 1), Rational(1, 1)], 
#        [Rational(1, 1), Rational(2, 1), Rational(4, 1), Rational(1, 1), Rational(-1, 1)]]

# for i in range(len(mat)): 
#     for j in range(len(mat[i])):
#         print(mat[i][j], end="    "),
#     print("")

# x = better(mat)
# print("\nAnswer: ")
# for i in range(len(x)): 
#     print(x[i], end="   " ) 
# print("\n")



# mat = [[Rational(2, 1), Rational(4, 1), Rational(-2, 1), Rational(-2, 1), Rational(-4, 1)], 
#      [Rational(1, 1), Rational(2, 1), Rational(4, 1), Rational(-3, 1), Rational(5, 1)], 
#      [Rational(-3, 1), Rational(-3, 1), Rational(8, 1), Rational(-2, 1), Rational(7, 1)], 
#      [Rational(-1, 1), Rational(1, 1), Rational(6, 1), Rational(-3, 1), Rational(7, 1)]]

# for i in range(len(mat)): 
#     for j in range(len(mat[i])):
#         print(mat[i][j], end="    "),
#     print("")

# x = better(mat)
# print("\nAnswer: ")
# for i in range(len(x)): 
#     print(x[i], end="   " ) 
# print("\n")
