import numpy as np
from math import e

def simps(f,a,b,N=50):
   
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    l=1
    n1=int(((b-a)/dx)/2)  
    for i in range(n1):
      nf=(dx/3*(y[+0]+4*y[+1]+y[+2]))
      y=y[2:]  
      print('Integral for a step',l,'=',nf)
      l+=1

   
    return 'final result: ' +str(S)