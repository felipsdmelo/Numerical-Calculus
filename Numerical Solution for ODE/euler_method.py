def euler_method(x0, y0, xf, h, f) :
    '''
    x0 - initial value of x
    y0 - initial value of y
    xf - final value of x
    h - size of the intervals
    f - function of x and y
    '''
    n = int ((xf - x0) / h) # number of iterations
    x = x0
    y = y0
    for i in range(n) :
        yf = y + h * f(x, y)
        x += h
        y = yf
    return yf
