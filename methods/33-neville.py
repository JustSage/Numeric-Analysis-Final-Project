
def neville(datax, datay, x):
    """
    Finds an interpolated value using Neville's algorithm.
    Input
      datax: input x's in a list of size n
      datay: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """
    n = len(datax)#n is the degree of the polynomial
    p = n*[0]# creates the zero matrix p
    for k in range(n):#runs loop from k equals 1 until it reaches end value
        l = k
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:#evaluates each element of the matrix
                p[i] = ((x-datax[i+k])*p[i]+
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
                print("p", l, i, "=", p[i])
                l += 1
        print("----------")
    return p[0]#result
#code source:https://github.com/gisalgs/geom/blob/master/neville.py#L23



dx=[2,2.25,2.3,2.7]
dy=[0,0.112463,0.167996,0.222709]
print("x = ",2.4,"y = ",neville(dx,dy,2.4))