# question 8

from methods.bisection2 import bisearch
from methods.newton2 import newtsearch
from methods.simpson import simps
from methods.romberg import *
from math import *
from sympy import *

x =symbols('x')
f= (sin(2*e**(-2*x)))/(x**2+5*x+6)
ft=f.diff(x)
f=lambdify(x,f)
ft=lambdify(x,ft)

#1.a)
print("\nBisection method:")
bisearch(f, -1, 2)
print("---------------------------")

#1.b)
print("\nNewton Raphson method:")
newtsearch(f,ft, -1, 2)
print("---------------------------")

#2.a)
print("\nSimpson method:\n")
print(simps(f,-0.4,0.4,6))
print("---------------------------")

#2.b)
print("\nRomberg method:\n")
p_rows = 4
I = romberg(f, -0.4, 0.4,4)
solution = I[p_rows-1, p_rows-1]
print(solution)
print("---------------------------")