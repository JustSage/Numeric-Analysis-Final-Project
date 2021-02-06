"""

    Natural cubic spline.

"""

import numpy as np
from methods.wikipedia_gauss_seidel import gauss_seidel
from math import pi


def natural_cubic_spline(points):
    """ Finds the natural cubic spline of a function given
    :param points:      An array of point tuples (xi, yi)
    :return:            A function
    """
    # lengths of intervals between points
    h = tuple(points[i+1][0] - points[i][0] for i in range(len(points) - 1))
    # the matrix that will hold the stuff for the stuff
    A = np.array([[0. for i in range(len(points))] for i in range(len(points))])

    # no, don't ask me how this thing works, I neither know nor care to know

    # unnecessary greek alphabet soup that's forced on people for no reason
    lamb = list(0 for i in range(len(h)))
    myu = list(0 for i in range(len(h)))
    for i in range(1, len(h)):
        lamb[i] = h[i] / (h[i] + h[i-1])
        myu[i-1] = 1 - lamb[i]

    # calculate the d values
    d = list()
    d.append(0)
    for i in range(1, len(points) - 1):
        val = 6 / (h[i-1] + h[i]) *\
              ((points[i+1][1] - points[i][1]) / h[i] -
               (points[i][1] - points[i-1][1]) / h[i-1])
        d.append(val)
    d.append(0)

    # fill the matrix
    for i in range(len(A)):
        A[i][i] = 2
    for i in range(len(lamb)):
        A[i][i+1] = lamb[i]
    for i in range(len(myu)):
        A[i+1][i] = myu[i]

    print("The resulting matrix for finding the second derivatives is:\n", A)
    print("The resulting thing that's on the other side of the equation is:\n", d)

    M = gauss_seidel(A, d)

    print("The M values are:\n", M)

    def si(x):
        # x is out of the bounds of the points we have (below lower)
        if points[0][0] > x:
            return None
        for i in range(len(points)):
            if points[i+1][0] >= x:
                # we found the range we are in

                # get the variables for the spline
                M1 = M[i]
                M2 = M[i+1]
                f1 = points[i][1]
                f2 = points[i+1][1]
                x1 = points[i][0]
                x2 = points[i+1][0]
                height = h[i]

                # strings for the three parts of the equation
                part1 = "(({0}-x)^3 * {1} + (x-{2})*{3}) / (6*{4})".format(x2, M1, x1, M2, height)
                part2 = "(({0}-x)*{1} + (x-{2})*{3}) / {4}".format(x2, f1, x1, f2, height)
                part3 = "((({0}-x)*{1} + (x-{2})*{3})/6)*{4}".format(x2, M1, x1, M2, height)

                # print the string of the spline equation
                print("Si(x) = \n", part1, " + \n", part2, " + \n", part3)

                # calculate the parts of the equation with the given x
                p1 = M1*((x2-x)**3) + M2*((x-x1)**3)
                p1 /= (6*height)

                p2 = f1*(x2-x) + f2*(x-x1)
                p2 /= height

                p3 = M1*(x2-x) + M2*(x-x1)
                p3 /= 6
                p3 *= height

                # return the solution
                return p1+p2-p3
        # x is out of the bounds of the points we have (above upper)
        return None
    return si


if __name__ == "__main__":
    # driver code
    pts = ((0, 0), (pi/6, 0.5), (pi/4, 0.7072), (pi/2, 1))
    spline = natural_cubic_spline(pts)
    if spline is not None:
        print("s(pi/3) = ", spline(pi/3))
    else:
        print("Something went wrong.")
