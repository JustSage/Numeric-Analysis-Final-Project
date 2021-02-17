import numpy as np
from math import e

def simps(f,a,b,N=50):
   '''Approximate the integral of f(x) from a to b by Simpson's rule.
        Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
        (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
        where x_i = a + i*dx and dx = (b - a)/N.
        Parameters
        ----------
        f : function
            Vectorized function of a single variable
        a , b : numbers
            Interval of integration [a,b]
        N : (even) integer
            Number of subintervals of [a,b]

        Returns
        -------
        float
            Approximation of the integral of f(x) from a to b using
            Simpson's rule with N subintervals of equal length'''
   
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)#Define function
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    l=1
    n1=int(((b-a)/dx)/2)  
    for i in range(n1):
      nf=(dx/3*(y[+0]+4*y[+1]+y[+2]))
      y=y[2:]  
      print('Integral for a step',l,'=',nf)#Value of the integration
      l+=1

    return 'final result: ' +str(S)
