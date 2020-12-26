from sympy import *


max_attempts = 10
pre_prompt = ">> "


def read_func():
    """Reads a mathematical function with an x variable from the user.
    :return:                The function
    """
    input_string = input(pre_prompt + "Enter a function using python syntax:\n>> ")
    expr = sympify(input_string)
    x = var('x')
    y = var('y')
    return lambda a, b: expr.subs(x, a).subs(y, b)


# unused stuff that I will not remove, because reasons


class Polynomial:
    """A polynomial with two variables"""

    def __init__(self, cons, x_deg, y_deg):
        """Constructor.
        :param cons:    A list of constants.
        :param x_deg:   A list of the degrees of the x variable.
        :param y_deg:   A list of the degrees of the y variable.
        """
        # copy lists over
        self.cons = list(cons)
        self.x_deg = list(x_deg)
        self.y_deg = list(y_deg)

    def degree(self):
        """The degree of the polynomial, based on the maximum between the
degrees of both variables.
        :return:        The degree.
        """
        return max(max(self.x_deg), max(self.y_deg))

    def get_func(self):
        """Returns a function of the polynomial.
        :return:        The function.
        """
        def f(x, y):
            constants = self.cons
            x_degrees = self.x_deg
            y_degrees = self.y_deg
            sum = 0
            for i in range(len(constants)):
                sum += constants[i] * x**x_degrees[i] * y**y_degrees[i]
            return sum
        return f

    def __str__(self):
        """Returns a string representation of the polynomial.

        :return:        The string.
        """
        ret_str = ""
        for i in range(len(self.cons)):
            if self.cons[i] == 0:
                continue
            a = str(self.cons[i])
            x = "x^" + str(self.x_deg[i])
            y = "y^" + str(self.y_deg[i])
            curr = a
            if self.x_deg[i] > 0:
                curr += " * " + x
            if self.y_deg[i] > 0:
                curr += " * " + y
            ret_str += curr
            if i < len(self.cons) - 1:
                ret_str += " + "
        return ret_str


def read_polynomial():
    """Reads a polynomial from the user.
    :return:            a function that returns the value of the polynomial for
the given x and y values.
    """
    num = read_int("Enter the number of constants in the function:")
    a = []
    x_deg = []
    y_deg = []

    for i in range(num):
        a.append(read_int("Enter the constant:"))
        x_deg.append(read_int("Enter the degree of the x variable:"))
        y_deg.append(read_int("Enter the degree of the y variable:"))

    return Polynomial(a, x_deg, y_deg)


def read_int(prompt):
    """Reads an integer from the user
    :param prompt:      The message prompt for the input.
    :return:            An integer from the user.
    """
    for i in range(max_attempts):
        try:
            return int(input(pre_prompt + prompt + "\n" + pre_prompt))
        except ValueError:
            print(pre_prompt + "Please enter a number.")
    raise IOError("Failed to read number.")


def read_float(prompt):
    """Reads a floating point number from the user
    :param prompt:      The message prompt for the input.
    :return:            An integer from the user.
    """
    for i in range(max_attempts):
        try:
            return float(input(pre_prompt + prompt + "\n" + pre_prompt))
        except ValueError:
            print(pre_prompt + "Please enter a floating point number.")
    raise IOError("Failed to read number.")


def test():
    """Driver function"""
    f = read_polynomial()
    print(f)
    print(f.get_func()(4, 4))
