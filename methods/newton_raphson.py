import math
import modules.modules as ui

def newton_raphson(self,f,df,a,b,tol=0.0001):
    """
    The newton raphson method is a root-finding algorithm that which produces
    successively better approximations to the roots (or zeroes) of a real-valued function.

    This version of the newton raphson method  starts with a single-variable function f
    defined for a real variable x, the function's derivative df, and an initial guess x0 for a root of f.

    If the function satisfies sufficient assumptions and the initial guess is close, 
    then x1 = x0 - f(x0)/df(x0) until sufficiently precise value is reached.

    It has the best convergance rate out of all the root finding methods as it's quadratic (2)
    The issues with this method are that sometimes the derivative will take a long time to compute,
    and if you don't assume the right area (to find the root), the method can diverge or overshoot.

    :param f: given function.
    :param df: derivative of given function.
    :param a: starting inverval.
    :param b: end invterval.
    :param tol: tolerance (epsilon), function converges to tolerance.
    :param max_iter: maximum iterations, if passed the secant method diverges.

    :return x: the returned root.
    :return count: the amount of iterations to find xr.
    """
    table = ui.Table(["iteration","df(x)","f(x)","x"])
    count = 0

    x = (a+b)/2.0 
    nr = f(x) / df(x) 
    table.append_row([str(count) + " - init",round(df(x),5),round(f(x),5),round(x,5)])

    while abs(nr) >= tol or math.isclose(f(x),0.0,abs_tol=tol) is False:
        # newton method iteration
        nr = f(x)/df(x) 
        x -= nr

        count += 1  
        table.append_row([count,round(df(x),5),round(f(x),5),round(x,5)])

    # print the results in a table
    table.show_table(color=(26,156,171))
    return x,count



