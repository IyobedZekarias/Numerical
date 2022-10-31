from Work.Rational import Rational

def f(x):
    return Rational(1, 1) / (Rational(1, 1) + x**2)

def Splinecoef(t, y, z):
    n = len(t)
    h = [Rational(0, 1) for i in range(n)]
    b = [Rational(0, 1) for i in range(n)]
    u = [Rational(0, 1) for i in range(n)]
    v = [Rational(0, 1) for i in range(n)]
    for i in range(n-1):
        h[i] = t[i+1] - t[i]
        b[i] = (y[i+1] - y[i])/h[i]
    
    u[1] = 2 * (h[0] + h[1])
    v[1] = 6 * (b[1] - b[0])

    for i in range(2, n-1):
        u[i] = 2 * (h[i] + h[i-1]) - (h[i-1]**2) / u[i-1]
        v[i] = 6 * (b[i] - b[i-1]) - (h[i-1] * v[i-1]) / u[i-1]
    
    z[n-1] = Rational(0, 1)
    for i in range(n-2, 0, -1):
        z[i] = (v[i] - (h[i] * z[i+1])) / u[i]
    z[0] = Rational(0, 1)


def SplineEval(t, y, z, x):
    Splinecoef(t, y, z)
    n = len(t)
    for i in range(n-1, -1, -1):
        if x - t[i] >= Rational(0, 1): break
    
    h = t[i+1] - t[i]
    tmp = (z[i]/2) + ((x - t[i]) * (z[i+1] - z[i])) / (6 * h)
    tmp = (-1 * (h / 6)) * (z[i+1] + 2 * z[i]) + (y[i+1] - y[i]) / h + (x - t[i]) * (tmp)
    return y[i] + (x - t[i]) * (tmp)

# x = []
# y = [Rational(1 ,    1), Rational(941, 1000), Rational(8   ,   10), 
#     Rational(64 ,  100), Rational(5  ,   10), Rational(39  ,  100), 
#     Rational(307, 1000), Rational(246, 1000), Rational(2   ,   10), 
#     Rational(164, 1000), Rational(137, 1000), Rational(116 , 1000), 
#     Rational(1  ,   10), Rational(86 , 1000), Rational(75  , 1000), 
#     Rational(66 , 1000), Rational(58 , 1000), Rational(52  , 1000), 
#     Rational(47 , 1000), Rational(42 , 1000)]

# for i in range(20):
#     x.append(Rational(i, 4))

# z = [Rational(0, 1) for i in range(len(x))]
# print()

# val = SplineEval(x, y, z, Rational(125, 1000))
# print("S(.125) = ", val, " = ", val.numerator()/val.denominator())

# val = SplineEval(x, y, z, Rational(85, 100))
# print("S(.85) = ", val, " = ", val.numerator()/val.denominator())

# val = SplineEval(x, y, z, Rational(17, 8))
# print("S(2.125) = ", val, " = ", val.numerator()/val.denominator())

# val = SplineEval(x, y, z, Rational(37, 10))
# print("S(3.7) = ", val, " = ", val.numerator()/val.denominator())

# val = SplineEval(x, y, z, Rational(103, 25))
# print("S(4.12) = ", val, " = ", val.numerator()/val.denominator())

# print()

# xpt = Rational(125, 1000)
# val = abs(SplineEval(x, y, z, xpt) - f(xpt))
# print("| S(.125) - f(.125) | = ", val, " = ", val.numerator()/val.denominator())

# xpt = Rational(85, 100)
# val = abs(SplineEval(x, y, z, xpt) - f(xpt))
# print("| S(.85) - f(.85) | = ", val, " = ",
#       val.numerator()/val.denominator())

# xpt = Rational(17, 8)
# val = abs(SplineEval(x, y, z, xpt) - f(xpt))
# print("| S(2.125) - f(2.125) | = ", val, " = ",
#       val.numerator()/val.denominator())

# xpt = Rational(37, 10)
# val = abs(SplineEval(x, y, z, xpt) - f(xpt))
# print("| S(3.7) - f(3.7) | = ", val, " = ",
#       val.numerator()/val.denominator())

# xpt = Rational(103, 25)
# val = abs(SplineEval(x, y, z, xpt) - f(xpt))
# print("| S(4.12) - f(4.12) | = ", val, " = ",
#       val.numerator()/val.denominator())

# print()

# for i in z:
#     print(i)

