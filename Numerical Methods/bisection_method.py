import math

def bisection_method(a, b, f, precision) :
    """
    Defines an approximate value as root of a function f
    based on Bisection Method
    
    Arguments:
    a -- lower bound of the interval
    b -- upper bound of the interval
    f -- function we want to find the root
    precision -- accuracy of the estimate (ex.: 10**(-5), 10**(-8)...)
    
    Returns:
    An estimate for a root of f
    """
    # maximum number of iterations
    maximum = int(((math.log(b - a) - math.log(precision)) / math.log(2))) + 1
    
    for i in range(0, maximum) :
        p = (a + b) / 2
        if (f(p) == 0 or abs(f(p)) < precision) : # breakpoint
            return p
        if (f(a) * f(p) < 0) : 
            b = p
        else :
            a = p
        if ((i + 1) == maximum) : 
            return p
