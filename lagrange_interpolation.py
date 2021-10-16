def lagrange_function(p, list_x, index) :
    '''
    Calculates the Lagrange function for the given index

    p - point we want to approximate the value
    list_x - list containing the x coordinates
    index - Lagrange's function index
    '''
    point = list_x[index] # first x
    num = 1 # numerator
    den = 1 # denominator
    for x in list_x :
        if point == x :
            continue
        num *= p - x
        den *= point - x
        
    return num / den

def lagrange_method(list_x, list_y, p) :
    '''
    Calculates the polynomial interpolation of a point p
    using Lagrange polynomials

    Keyword arguments:
    list_x - list containing the x coordinates
    list_y - list containing the y coordinates
    p - point we want to approximate the value

    Returns:
    An estimate for f(p)
    '''
    deg = len(list_x) - 1 # degree
    approx = 0
    for i in range(deg + 1) :
        approx += list_y[i] * lagrange_function(p, list_x, i)
    return approx
