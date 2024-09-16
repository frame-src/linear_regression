def line(x:float, m:float,c:float) :
    y = ( m * x ) + c
    return y


def error(x:float, m:float, c:float, true_y:float) :
    y = line (x,m,c)
    return true_y - y


def squared_error_mean( x: list, y:list, m:float, c:float) :
    i = 0
    while i < len(x) :
        if i == 0 :
            pass
        e = error(x[i], m, c, y[i])
        tot = tot + ( e * e )
    return tot/(i - 1)


def derivatives_of_e_respect_to_c(x:list,y:list, m:float, c:float) :
    tot = 0
    i = 0
    while i < len(x) :
        if i == 0 :
            pass
        else:
            e = error (x[i], m,c,y[i])
            tot = tot + e
        i = i + 1
    return (-2 * tot) / (i - 1)


def derivatives_of_e_respect_to_m (x:list, y: list, m:float, c:float ) :
    tot = 0
    i = 0
    while i < len(y) :
        if i == 0 :
            pass

        else:
            e = error(x[i], m,c,y[i])
            tot = tot + ( e * x[i] )
        i = i + 1
    return (-2 * tot) / (i - 1)


def calculate_min(x:list):
    minimum = float(x[1])
    i : int = 1
    while i < len(x):
        if minimum < float(x[i]):
            minimum = float(x[i])
        i = i + 1
    return minimum


def normalize_data(x: list):
    min_x = x[1]
    max_x = x[1]
    i = 1
    while i < len (x):
        if x[i] < min_x:
            min_x = x[i]
        if x[i] > max_x:
            max_x = x[i]
        i = i + 1
    norm = max_x - min_x
    i = 1
    while i < len(x):
        x[i]  = (x[i] - min_x )/norm
        i = i + 1
    return x
