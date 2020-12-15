from numproj import n_point_double_integral
from userInput import read_polynomial, read_float
from math import ceil


def main():
    try:
        poly = read_polynomial()
        a = read_float("Enter the lower bound of the integral for y.")
        b = read_float("Enter the upper bound of the integral for y.")
        c = read_float("Enter the lower bound of the integral for x.")
        d = read_float("Enter the upper bound of the integral for x.")
        result = n_point_double_integral(poly.get_func(), a, b, c, d, ceil(poly.degree() / 2))
        print("The approximation of the integral is " + str(result))
    except IOError as e:
        print(e)


main()
