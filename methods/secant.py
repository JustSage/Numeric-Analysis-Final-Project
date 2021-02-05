import modules.modules as ui

def secant_method(f,a,b,tol=0.0001,max_iter=100):
    """
    The secant method is a root-finding algorithm that uses a 
    succession of roots of secant lines to better approximate a root of a function f.

    The iterates xr of the secant method converge to a root of f if the initial
    values x0 and x1 are sufficiently close to the root.
    It's convergence is roughly equals to 1.618, the golden ratio.

    The secant method does not always converge, and is not always bracketed,
    but comaring to the newton method, it can handle functions that are not easily derived,
    saving processing time.
    
    :param f: given function
    :param a: initial guess (interval)
    :param b: second guess (interval)
    :param tol: tolerance (epsilon), function converges to tolerance.
    :param max_iter: maximum iterations, if passed the secant method diverges.

    :return xr: the returned root
    :return count: the amount of iterations to find xr.
    """
    table = ui.Table(["iteration","xi","xi+1","f(xi)"])
    count,xr = 0,0
    x0, x1 = a,b

    try:
        if f(x0) == f(x1):
            raise ValueError("This will lead to a division by Zero!")
    except ValueError as message: 
        print(message)

    table.append_row([str(count) + " - init",round(x0,5),round(x1,5),round(f(x0),5)])
    while count < max_iter:
        # secant method iteration
        try:
            xr = x1 - f(x1)* ((x1 - x0)/(f(x1) - f(x0))) 
            raise ZeroDivisionError("Numerator divided by zero")
        except ZeroDivisionError as message:
            print(message)

        if abs(xr - x1) < tol: 
            break 

        else:
            x0, x1 = x1, xr
            count+=1 
            table.append_row([count,round(x0,5),round(x1,5),round(f(x0),5)])


    # print the results in a table
    table.show_table(color=(26,156,171))

    return xr
 