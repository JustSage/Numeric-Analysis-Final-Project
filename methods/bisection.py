import numpy as np
def bisection(f,a,b,tol,max_iter):
    """
    :param f: - a polynomial function
    :param a: - range of inspection starting point
    :param b: - range of inspection ending point
    :param tol: - tolerance given (epsilon)
    :param max_iter: - amount of iterations the algorithm is still efficient.
    
    :return mid: - a suspicious root.

    The bisection method is a root-finding method that applies to any continuous
    functions for which one knows two values with opposite signs.
    The method consists of repeatedly bisecting the interval 
    defined by these values and then selecting the subinterval in which the function changes sign,
    and therefore must contain a root.
    """
    xl, xr = a, b
    mid,count = 0,0

    while np.abs(xr-xl) >= tol:
        mid = (xl+xr)/2.0
        if f(xl)*f(mid) > 0: xl = mid
        else: xr = mid
        count += 1 
    if(count > max_iter):
        print("Bisection method is not efficient for this function")
        print(f"{count} > {max_iter}")
    return mid