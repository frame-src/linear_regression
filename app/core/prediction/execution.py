from core.utils.fileio import load_model
import json

def make_prediction(num:float, model_name: str) -> tuple[float, str]:
    model = load_model(model_name)
    if model is None:
        return None, None
    else:
        try:
            model = json.loads(model)
        except:
            print("model not a valid Json")
            return None, None
    m = float(model['m'])
    c = float(model['c'])
    label = str(model['label'])
    y = m * num + c
    return y, label