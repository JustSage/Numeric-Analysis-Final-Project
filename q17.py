# question 17

from methods.bisection2 import bisearch
from methods.newton2 import newtsearch
from math import *
from sympy import *

x =symbols('x')
f= (x**2*e**(-x**2-5*x-3))*(3*x-1)
ft=f.diff(x)
f=lambdify(x,f)
ft=lambdify(x,ft)

#a.1)
print("\nBisection method:")
bisearch(f,ft, 0, 3)
print("---------------------------")
#a.2)
print("\nNewton Raphson method:")
newtsearch(f,ft, 0, 3)
print("---------------------------")