def trapezoidal_rule(a, b, n, f) :
    '''
    Keyword arguments:
    a -- lower bound of the interval
    b -- upper bound of the interval
    n - number of subintervals
    f - function of x

    Returns:
    An estimate for the definite integral of f
    '''
    
    h = (b - a) / n # subinterval height
    
    if (n == 1) :
        return h / 2 * (f(a) + f(b))
    
    values = [0 for i in range(n + 1)]
    # values = [0] * n
    for i in range(n + 1) : # correcting the values according to the method
        if (i == 0 or i == n) :
            values[i] = f(a + h * i)
        else :
            values[i] = 2 * f(a + h * i)
    return h / 2 * sum(values)

def trapezoidal_error(a, b, n, d) :
    '''
    Keyword arguments:
    a -- lower bound of the interval
    b -- upper bound of the interval
    n - number of subintervals
    d - second derivative of f

    Returns:
    Upper bound to the error of trapezoidal rule with n subintervals
    '''
    h = (b - a) / n
    h_aux = (b - a) / 100
    maximum = 0
    # searching for the maximum value of the second derivative of f in the interval
    for i in range(100) : # 100 subintervals
        if (abs(d(a + h_aux * i))) > maximum :
            maximum =  abs(d(a + h_aux * i))
    return (h**2 / 12) * (b - a) * maximum



