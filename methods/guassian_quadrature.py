import numpy

def n_point_double_integral(f, a, b, c, d, n=2):
    """double integral using n-point gauss method
    
    integral between -1 and 1 of f(x) = w0*f(x0) + w1*f(x1)
    
    :param f:       The function we want to integrate
    :param a:       The lower bound over the x axis.
    :param b:       The upper bound over the x axis.
    :param c:       The lower bound over the y axis.
    :param d:       The upper bound over the y axis.
    :param n:       The number of points to use.
    :return:        The value of the integral
    """
    # change the x and y values to fit an integral between -1 and 1
    g = lambda x: (d+c)/2+((d-c)/2)*x
    h = lambda y: (b+a)/2+((b-a)/2)*y
    
    # the legendre weights and values
    xs, cs = numpy.polynomial.legendre.leggauss(n)
    
    # the inner integral over x
    def inner_f(y):
        sum = 0
        for i in range(n):
            sum += cs[i] * f(g(xs[i]), y) * ((d-c) / 2)
        return sum
    
    # outer integral over y
    sum = 0
    for i in range(n):
        sum += cs[i] * inner_f(h(xs[i])) * ((b-a) / 2)
    return sum

