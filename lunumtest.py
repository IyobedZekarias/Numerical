from Library.lunum import ln, e, cos, sin, NaiveGauss, Gauss, bisection, secant, NewtonInterp, RichExtrap, Trapezoidal, Romberg, Simpson, Spline, Rand, MonteCarlo
from Library.Rational import Rational
import math

print("ln(3.5)---- \nas Rational: ", ln(Rational(35, 10)) , "\nand as a float: ", ln(3.5))
print()
print("e(3.5)----- \nas Rational: ", e(Rational(35, 10)), " as a float: ", e(3.5))
print()
print("cos(.25)----- \nas Rational: ", cos(Rational(1, 4)), " as a float: ", cos(.25))
print()
print("sin(.25)---- \nas Rational: ", sin(Rational(1, 4)), " as a float: ", sin(.25))
print()

x = [[2.2, 1.23, 45.2, 1.1, 2.1], 
     [1.2, 23.4, 12.5, 1.78, 1.9], 
     [453.1, 12.0, 7.8, 8.1, 6.89], 
     [34.4, 123.9, 12.33, 9.0, 1.1]]

xrat = [[Rational(22, 10), Rational(123, 100), Rational(452, 10), Rational(11, 10), Rational(21, 10)],
        [Rational(12, 10), Rational(234, 10), Rational(125, 10), Rational(178, 10), Rational(19, 10)],
        [Rational(4531, 10), Rational(12, 1), Rational(78, 10), Rational(81, 10), Rational(689, 100)],
        [Rational(344, 10), Rational(1239, 10), Rational(1233, 100), Rational(9, 1), Rational(11, 10)]]


ngflist = NaiveGauss(x)
ngrlist = NaiveGauss(xrat)

gflist = Gauss(x)
grlist = Gauss(xrat)

print("Gaussian elimination-----")
for i in x: 
    print(i)
print("\nNaive, float")
for i in ngflist: 
    print(i, end=", ")
print()
print("\nNaive, Rational")
for i in ngrlist: 
    print(i, end=", ")
print()
print("\nImproved, float")
for i in gflist: 
    print(i, end=", ")
print()
print("\nImproved, Rational")
for i in grlist: 
    print(i, end=", ")
print("\n")


def fn(x):
    return (x**5 + x**3 + 3)


print("bisection for function f(x) = x^5 + x^3 + 3-----\nas Rational: ", bisection(fn, Rational(-10, 1), Rational(10, 1)), "\nas float: ", bisection(fn, -10, 10))
print()
print("secant for function f(x) = x^5 + x^3 + 3------\nas Rational: ", secant(fn), "\nas float: ", secant(fn, type=float))
print()

x = []
y = [Rational(1 ,    1), Rational(941, 1000), Rational(8   ,   10),
    Rational(64 ,  100), Rational(5  ,   10), Rational(39  ,  100),
    Rational(307, 1000), Rational(246, 1000), Rational(2   ,   10),
    Rational(164, 1000), Rational(137, 1000), Rational(116 , 1000),
    Rational(1  ,   10), Rational(86 , 1000), Rational(75  , 1000),
    Rational(66 , 1000), Rational(58 , 1000), Rational(52  , 1000),
    Rational(47 , 1000), Rational(42 , 1000)]

for i in range(20):
    x.append(Rational(i, 4))

xflt = [i.numerator()/i.denominator() for i in x]
yflt = [i.numerator()/i.denominator() for i in y]

print("Newton Interpolation for x = 1.256 for points--------\n x:", xflt, "\n y: ", yflt)

print("Rational: ", NewtonInterp(Rational(1256, 1000), x, y), "\nFloat: ", NewtonInterp(1.256, xflt, yflt))
print()

print("Spline Interpolation for x = 1.256 for points--------\n x:", xflt, "\n y: ", yflt)

print("Rational: ", Spline(Rational(1256, 1000), x, y),
      "\nFloat: ", Spline(1.256, xflt, yflt))
print()


print("Richardson Extrapolation for x = 1.2456433 for f(x) = cos(x)-------\nas Rational: ",
      RichExtrap(cos, Rational(31141, 25000), l=0, u=10)[9][9], "\nas Float: ", RichExtrap(cos, 1.2456433, l=0, u=10)[9][9])

print()
print("Trapezoidal Integration for f(x) = cos(x) from 0 to 14-------\nas Rational: ",
      Trapezoidal(cos, Rational(0, 1), Rational(14, 1)), "\nas Float: ", Trapezoidal(cos, 0.0, 14.0))

print()
print("Romberg Integration for f(x) = sin(x) from 0 to 14-------\nas Rational: ",
      Romberg(sin, Rational(0, 1), Rational(14, 1)), "\nas Float: ", Romberg(sin, 0.0, 14.0))

print()
print("Simpson Integration for f(x) = e^(x) from 0 to 5-------\nas Rational: ", Simpson(e,
      Rational(0, 1), Rational(5, 1), mlevel=5), "\nas Float: ", Simpson(e, 0.0, 5.0, mlevel=5))

print()
x = [0] * 20
Rand(x, 0, 1000, type=int, seed=2**61)
print("Random Numbers: \n", x)
print()


def mofun(args):
    return ((args[1]*args[0]+args[2]**2) + args[2] * e(args[1]) + cos(args[0]))


D = MonteCarlo(mofun, (0, 1), (-2, 3), (-1, 9), size=9000)
print("Monte Carlo ∫0 to 1 ∫-2 to 3 ∫-1 to 9 ((xy+z^2) + z * e^y + cos(x)) dxdydz = ", D)
print()


