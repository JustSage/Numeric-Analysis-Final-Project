# question 17

from methods.bisection2 import bisearch
from methods.newton2 import newtsearch
from methods.simpson import simps
from methods.romberg import *
from math import *
from sympy import *

x =symbols('x')
f= (x**2*e**(-x**2-5*x-3))*(3*x-1)
ft=f.diff(x)
f=lambdify(x,f)
ft=lambdify(x,ft)

#1.a)
print("\nBisection method:")
bisearch(f, 0, 3)
print("---------------------------")

#1.b)
print("\nNewton Raphson method:")
newtsearch(f,ft, 0, 3)
print("---------------------------")

#2.a)
print("\nSimpson method:\n")
print(simps(f,0.5,1,6))
print("---------------------------")

#2.b)
print("\nRomberg method:\n")
p_rows = 4
I = romberg(f, 0.5, 1,4)
solution = I[p_rows-1, p_rows-1]
print(solution)
print("---------------------------")