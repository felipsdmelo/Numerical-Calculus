def newton_raphson(p, f, df, precision, maximum) :
    """
    Defines an approximate value as root of a function f
    based on Newton-Raphson Method
    
    Keyword arguments:
    p -- initial point
    f -- function we want to find a root
    df -- derivative of f
    precision -- accuracy of the estimate (ex.: 10**(-5), 10**(-8)...)
    maximum -- maximum number of iterations
    
    Returns:
    An estimate for a root of f
    """
    
    for i in range(0, maximum) :
        next = p - (f(p) / df(p))
        if (abs(f(next)) < precision) :
            return next
        p = next

    return "Error" 
