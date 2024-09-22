from core.utils.parser import execute_parsing
from core.training.operations import translate_model, derivatives_of_e_respect_to_c, derivatives_of_e_respect_to_m,calculate_min, normalize_data
from core.utils.plot import plot_line_and_points, plot_points
from core.utils.error_handler import set_error

import copy

def linear_regression(x, y) -> tuple[float, float]:
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


def set_dependent_variable(list_one: list, list_two: list, dependent_variable_name: str) -> tuple[list, list]: 
    if list_one[0] == dependent_variable_name:
        return list_one, list_two
    elif list_two[0] == dependent_variable_name:
        return list_two, list_one
    set_error("Error: Not a valid dependent_variable, first column in dataset was set as default.")
    return list_two, list_one


def train_model(dataset_name: str = "default_data.csv", dependent_variable_name: str = "km") -> tuple[float, float]:
    print("Training with dataset name: " + dataset_name + "     ...")
    x, y = execute_parsing(dataset_name)
    if not x or not y :
        set_error("Error: Not a valid dataset.")
        return None
    x, y = set_dependent_variable(x, y, dependent_variable_name)
    copy_x = copy.deepcopy(x)
    copy_y = copy.deepcopy(y)
    normed_x = normalize_data(x)
    normed_y = normalize_data(y)
    m, c = linear_regression(normed_x,normed_y)
    print("_______________________________________________________________________________")
    print("BEST FIT :       Y = " + str(m) + " X " + str(c)) 
    print("_______________________________________________________________________________")
    plot_points(copy_x, copy_y, dataset_name)
    plot_line_and_points(normed_x, normed_y, m, c, dataset_name)
    m, c = translate_model( m, c, copy_x, copy_y)
    return m, c