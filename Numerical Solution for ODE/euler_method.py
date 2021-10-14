def euler_method(x0, y0, xf, h, f) :
    '''
    Approximates the value of an ODE using Euler's Method

    Keyword arguments:
    x0 - initial value of x
    y0 - initial value of y
    xf - final value of x
    h - size of the intervals (step)
    f - function of x and y (usually the right side of the equation)

    Returns:
    An estimate for the ODE
    '''
    n = int ((xf - x0) / h) # number of iterations
    x = x0
    y = y0
    yf = 0 # avoids local variable reference error
    for i in range(n) :
        yf = y + h * f(x, y)
        x += h
        y = yf
    return yf


def improved_euler_method(x0, y0, xf, h, f)
    '''
    Approximates the value of an ODE using Improved Euler's Method,
    also known as Heun's Method

    Keyword arguments:
    x0 - initial value of x
    y0 - initial value of y
    xf - final value of x
    h - size of the intervals (step)
    f - function of x and y (usually the right side of the equation)

    Returns:
    An estimate for the ODE
    '''
    n = int ((xf - x0) / h) # number of iterations
    x = x0
    y = y0
    yf = 0 # avoids local variable reference error
    for i in range(n) :
        yf = y + h/2 * (f(x, y) + f(x + h, y + h * f(x, y)))
        x += h
        y = yf
    return yf
