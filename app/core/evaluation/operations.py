def mean_squared_error( x: list, y:list, m:float, c:float) -> float :
    i = 0
    while i < len(x) :
        if i == 0 :
            pass
        e = error(x[i], m, c, y[i])
        tot = tot + ( e * e )
    return tot/(i - 1)
