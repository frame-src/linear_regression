def line(x:float, m:float,c:float) -> float:
    y = ( m * x ) + c
    return y


def error(x:float, m:float, c:float, true_y:float) -> float:
    y = line (x,m,c)
    return true_y - y


def derivatives_of_e_respect_to_c(x:list,y:list, m:float, c:float) -> float:
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


def derivatives_of_e_respect_to_m (x:list, y: list, m:float, c:float ) -> float:
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


def calculate_min(x:list) -> float:
    minimum = float(x[1])
    i : int = 1
    while i < len(x):
        if minimum < float(x[i]):
            minimum = float(x[i])
        i = i + 1
    return minimum


def normalize_data(x: list) -> list:
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


def translate_model(normed_m:float, normed_c:float, x:list, y:list) -> tuple[float,float]:
    min_y = min(y)
    max_y = max(y)
    min_x = min(x)
    max_x = max(x)

    m = translate_slope(normed_m, max_y, min_y, max_x, min_x)
    c = translate_intercept(normed_c, m, max_y, min_y, max_x, min_x)
    return m,c

def translate_slope(normed_m: float, max_y:float, min_y:float, max_x:float, min_x:float ) -> float:
    delta_y = max_y - min_y
    delta_x = max_x - min_x
    m = normed_m * (delta_y / delta_x)
    return m
 

def translate_intercept(normed_c:float, m:float, max_y:float, min_y:float, max_x:float, min_x:float) -> float:
    c = (normed_c * (max_y - min_y)) + min_y - (m * min_x)
    return c
