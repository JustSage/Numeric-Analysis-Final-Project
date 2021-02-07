def newtonraph(f,ft,a,b):
    """
    newton raphson
    """
    print('\nApplying Newton Raphson method from (%0.1f) to (%0.1f):' % (a, b))
    xn = (a+b)/2
    for n in range(0,500):
        fxn = f(xn)
        if abs(fxn) < 0.00001:
            print(n, "Iterations, x=",round(xn, 4))
            return round(xn, 4)
        ftxn = ft(xn)
        if ftxn == 0:
            return None
        xn = xn - fxn/ftxn
    return None

def newtsearch(f,ft, x0, x1):    #goes by steps of 0.1 and checks for sign changed, activates bisection function
    answers=[]                 #when found.
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
