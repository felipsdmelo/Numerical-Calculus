from math import *

def f(x, y) :
    return sin(x * y)

def runge_kutta_third_order(x0, y0, xf, h, f) :
    '''
    Approximates the value of an ODE using Runge-Kutta's
    third order method

    Keyword arguments:
    x0 - initial value of x
    y0 - initial value of y
    xf - final value of x
    h - size of the intervals (step)
    f - function of x and y (usually the right side of the equation)

    Returns:
    An estimate for the ODE
    '''
    n = int((xf - x0) / h) # number of iterations
    x = x0
    y = y0
    yf = 0 # avoids local variable reference error
    for i in range(n) :
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + 3 * h / 4, y + 3 * k2 / 4)
        yf = y + 1 / 9 * (2 * k1 + 3 * k2 + 4 * k3)
        x += h
        y = yf
    return yf
