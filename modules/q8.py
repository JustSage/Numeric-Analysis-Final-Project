# question 8

from methods.bisection2 import bisearch
from methods.newton2 import newtsearch
from math import *
from sympy import *

x =symbols('x')
f= (sin(2*e**(-2*x)))/(x**2+5*x+6)
ft=f.diff(x)
f=lambdify(x,f)
ft=lambdify(x,ft)

#a.1)
print("\nBisection method:")
bisearch(f,ft, -1, 2)
print("---------------------------")
#a.2)
print("\nNewton Raphson method:")
newtsearch(f,ft, -1, 2)
print("---------------------------")