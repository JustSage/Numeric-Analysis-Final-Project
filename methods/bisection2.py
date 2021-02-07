from sympy import *

def bisection(f, x0, x1):  #uses the method we learned in class
    iteration = 1
    print('\nBisecting from (%0.1f) to (%0.1f):' % (x0, x1))
    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print('i(%d): x=(%0.6f), f(x)=(%0.6f)' % (iteration, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        iteration = iteration + 1
        condition = abs(f(x2)) > 0.00001
    print('Root: (%0.8f)' % x2)
    return x2

def bisearch(f,ft, x0, x1):    #goes by steps of 0.1 and checks for sign changed, activates bisection function
    answers=[]                 #when found.
    basecheck=0
    flag=x0
    follow=x0+0.1
    while flag<= x1:
        if f(flag) * f(follow) < 0.0:
            basecheck = basecheck+1
            answers.append(bisection(f,flag, follow))
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



