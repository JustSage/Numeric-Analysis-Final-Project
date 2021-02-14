import numpy as np
from math import e
import numpy as np

def trapezcomp(f, a, b, n):
    """
    Composite trapezoidal function integration

    INPUTS:
    f:  the function to integrate
    a:  lower bound of integration
    b:  upper bound
    n:  number of panels to create between ``a`` and ``b``
    """

    # Initialization
    h = (b - a) / n
    x = a

    # Composite rule
    In = f(a)
    for k in range(1, n):
        x  = x + h
        In += 2*f(x)

    return (In + f(b))*h*0.5

def romberg(f, a, b, p):
    """
    Romberg integration

    INPUTS:
    f:  the function to integrate
    a:  lower bound of integration
    b:  upper bound
    p:  number of rows in the Romberg table
    """

    I = np.zeros((p, p))
    for k in range(0, p):
        # Composite trapezoidal rule for 2^k panels
        I[k, 0] = trapezcomp(f, a, b, 2**k)

        # Romberg recursive formula
        for j in range(0, k):
            I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)

        print(I[k,0:k+1])   # display intermediate results

    return I


#code source :https://learnche.org/3E4/Numerical_differentiation_and_integration