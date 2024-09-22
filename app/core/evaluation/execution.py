from core.utils.fileio import load_model
from core.utils.error_handler import set_error
from core.utils.parser import execute_parsing
from core.evaluation.operations import error, abs_value
import json

def mean_squared_error( x: list, y:list, m:float, c:float) -> float :
    tot = 0
    i = 1
    while i < len(x) :
        e = error(x[i], y[i], m, c)
        tot = tot + ( e * e )
        i = i + 1 
    return tot/(i - 1)


def mean_absolute_error( x: list, y:list, m:float, c:float) -> float :
    tot = 0
    i = 1
    while i < len(x) :
        e = error(x[i], y[i], m, c)
        tot = tot + ( abs_value(e) )
        i = i + 1 
    return tot/(i - 1)


def evaluate_model(model_name:str = 'model'):
    model = load_model(model_name)
    if model is None:
        set_error("Model not found")
        return None
    else:
        try:
            model = json.loads(model)
        except:
            set_error("Model not a valid Json")
            return None
    m = float(model['m'])
    c = float(model['c'])
    label = str(model['label'])
    # dataset_name = str(model['dataset_name'])
    x, y = execute_parsing()
    if x[0] != label :
        tmp_list = x
        x = y
        y = tmp_list
    mse = mean_squared_error(x, y, m, c)
    mae = mean_absolute_error(x, y, m, c)
    return mse, mae
    


    
