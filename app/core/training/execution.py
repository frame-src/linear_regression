from core.utils.parser import execute_parsing
from core.training.operations import derivatives_of_e_respect_to_c, derivatives_of_e_respect_to_m,calculate_min, normalize_data
from core.utils.plot import plot_line_and_points

import copy

def linear_regression(x, y):
    epoch = 100
    i = 0
    m = 0
    c = 0
    L = 1

    while i < epoch:
        if i == 0:
            pass
        else: 
            m = m - L * derivatives_of_e_respect_to_m(x, y, m, c)
            c = c - L * derivatives_of_e_respect_to_c(x, y, m, c)
        i = i + 1
    return m,c


def execute(dataset_name: str = "default_data.csv"):
    print("Training with dataset name: " + dataset_name)
    x, y = execute_parsing(dataset_name)
    if not x or not y :
        print("not a valid dataset...")
        return None
    copy_x = copy.deepcopy(x)
    copy_y = copy.deepcopy(y)
    normed_x = normalize_data(x)
    normed_y = normalize_data(y)
    m, c = linear_regression(normed_x,normed_y)
    print("best fit :    Y = " + str(m) + " X " + str(c)) 
    plot_line_and_points(x, y, m, c)
    minimum = calculate_min(copy_x)
    c = c + minimum
    return m, c