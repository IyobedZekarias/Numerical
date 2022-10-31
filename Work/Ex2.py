from Work.Rational import Rational

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


xpt = [Rational(1, 1), Rational(5, 4), Rational(3, 2), Rational(7, 4), Rational(2, 1)]
ypt = [Rational(10, 1), Rational(8, 1), Rational(7, 1), Rational(6, 1), Rational(5, 1)]

# print("\nNewton Interpolation ------------- ")
n = NDD(xpt, ypt)
# print("f(2.5) = ", poly(Rational(5, 2), xpt, n))


def Simpson(a, b, tol, level, level_max):
    level += 1
    h = (b - a)
    c = (a + b) / Rational(2, 1)
    oneSimpson = (h * (poly(a, xpt, n) + (Rational(4, 1) * poly(c, xpt, n)) + poly(b, xpt, n))) / Rational(6, 1)
    d = (a + c) / Rational(2, 1)
    e = (c + b) / Rational(2, 1)
    twoSimpson = (h * (poly(a, xpt, n) + (Rational(4, 1) * poly(d, xpt, n)) + (Rational(2, 1)
                                                         * poly(c, xpt, n)) + (Rational(4, 1) * poly(e, xpt, n)) + poly(b, xpt, n))) / Rational(12, 1)

    if level >= level_max:
        return twoSimpson
    else:
        if (abs(twoSimpson - oneSimpson) < tol):
            return twoSimpson + ((twoSimpson - oneSimpson) / Rational(15, 1))
        else:
            lSimp = Simpson(a, c, tol/Rational(2, 1), level, level_max)
            rSimp = Simpson(c, b, tol/Rational(2, 1), level, level_max)
            return lSimp + rSimp


ans = Simpson(Rational(1, 1), Rational(2, 1), Rational(.5, 10**5), 0, 4)
print(ans, " = ", ans.numerator()/ans.denominator())
