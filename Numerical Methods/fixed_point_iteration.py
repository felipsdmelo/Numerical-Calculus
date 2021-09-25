def fixed_point(a, b, f, phi, precision, maximum) :
    """
    Defines an approximate value as root of a function f
    based on Fixed-Point Iteration
    
    Keyword arguments:
    a -- lower bound of the interval
    b -- upper bound of the interval
    f -- function we want to find a root
    phi -- funtion phi(x) [manipulate f so that x = phi(x)]
    precision -- accuracy of the estimate (ex.: 10**(-5), 10**(-8)...)
    maximum -- maximum number of iterations
    
    Returns:
    An estimate for a root of f
    """
    
    p = (a + b) / 2
    for i in range(0, maximum) :
        if (f(phi(p)) == 0 or abs(f(phi(p))) < precision) :
            return p
        p = phi(p)
        
