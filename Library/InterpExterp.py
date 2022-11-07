from Library.Rational import Rational


xpt = [Rational(2, 1), Rational(3, 1), Rational(5, 1), Rational(6, 1)]
ypt = [Rational(15713, 1e4), Rational(15719, 1e4),
       Rational(15738, 1e4), Rational(15731, 1e4)]
# Newton’s Divided difference, produces coefficients of
# interpolating polynomial


def zerolistmaker(n):
    listofzeros = [Rational(0, 1)] * n
    return listofzeros


def NDD(x, y):
    n = len(x)
    A = zerolistmaker(n)
    for i in range(n):
        A[i] = zerolistmaker(n+1)
    for i in range(n):
        A[i][0] = x[i]
        A[i][1] = y[i]

    for j in range(2, n+1):
        for i in range(j-1, n):
            A[i][j] = (A[i][j-1]-A[i-1][j-1]) / (A[i][0]-A[i-j+1][0])
    # Copy diagonal elements into array for returning
    p = zerolistmaker(n)
    for k in range(0, n):
        p[k] = A[k][k+1]
    return p


# Evaluates polynomial at ’t’ given x-values and coefficients
def poly(t, x, p):
    n = len(x)
    out = p[n-1]
    for i in range(n-2, -1, -1):
        out = out*(t-x[i]) + p[i]
    return out


# print("\nNewton Interpolation ------------- ")
# n = NDD(xpt, ypt)

# print("f(2.5) = ", poly(Rational(5, 2), xpt, n))
# print("f(4)   = ", poly(Rational(4, 1), xpt, n))
# print("f(5.8) = ", poly(Rational(29, 5), xpt, n))


# print("\nRichardson extrapolation ------------- ")


def phi(f, x, h):
    return((
        f(x+h) -
        f(x-h)) / (Rational(2, 1) * h)
    )

def Ext(function, x, lowerbound, upperbound):
    d = [phi(function, x, h)
        for h in [Rational(1, 2)**n
                for n in range(lowerbound, upperbound)]]

    D = zerolistmaker(len(d))
    for i in range(len(d)):
        D[i] = zerolistmaker(len(d))
        D[i][0] = d[i]

    four = Rational(4, 1)
    for m in range(1, len(d)):
        for n in range(m, len(d)):
            D[n][m] = (four**m * D[n][m-1] - D[n-1][m-1]) / (four**m - 1)

    return D



# print()
