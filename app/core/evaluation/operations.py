def error(x:float, measured_y:float, m:float, c:float) -> float:
    y = (m * x) + c
    return measured_y - y

def abs_value(num:float) -> float:
    if num > 0:
        return num
    else :
        return -1 * num

