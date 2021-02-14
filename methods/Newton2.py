def newtonraph(f,ft,a,b):
    """

    :param f: polynomial function
    :param ft: derivative of our function
    :param a: lower range
    :param b: upper range
    :return:
    returns a suspected root in the range.

    This function preforms the newton raphson method we learned in class. We start with a single variable xn which
    is the middle of our range and will be our initial guess for the root. Then we calculate f(xn) and ft(xn) and
    calculate [new]xn=[old]xn-(f(xn)/ft(xn)). We continue doing so iteratively, getting closer and closer to our answer
    until the we are precise enough to the real answer.
    """
    print('\nApplying Newton Raphson method from (%0.1f) to (%0.1f):' % (a, b))
    xn = (a+b)/2
    for n in range(0,500):
        fxn = f(xn)
        print('i(%d): x=(%0.6f), f(x)=(%0.6f)' % (n+1, xn, fxn))
        if abs(fxn) < 0.00001:
            print(n+1, "Iterations, x=",round(xn, 4))
            return round(xn, 4)
        ftxn = ft(xn)
        if ftxn == 0:
            return None
        xn = xn - fxn/ftxn
    return None

def newtsearch(f,ft, x0, x1):
    """
       :param f: polynomial function
       :param ft: derivative of our function
       :param x0: lower range
       :param x1: upper range
       :return: all the roots in the given range

       goes by steps of 0.1 and checks for sign changed, activates bisection function when found.
       basically splitting our given range into lots of small sub-ranges ro run the bisection function on.
       """
    answers=[]
    basecheck=0
    flag=x0
    follow=x0+0.1
    while flag<= x1:
        if f(flag) * f(follow) < 0.0:
            basecheck = basecheck+1
            answers.append(newtonraph(f,ft ,flag, follow))
        flag = follow
        follow = follow + 0.1
    if f(0)==0:
        basecheck = basecheck + 1
        answers.append(0)
        print("\nChecking (x=0):\ni(1): x=(0),f(x)=(0)\nRoot: (0)")
    if basecheck==0:
        print('\nNo suspected roots found.')
    else:
        shortanswers = []
        for a in answers:
            shortanswers.append(('%0.2f' % a))
        print('\nThe roots are:', shortanswers)
