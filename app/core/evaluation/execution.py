from core.utils.fileio import load_model


def make_prediction(num:float, model_name: str) :
    model = load_model(model_name)
    if model is None:
        return None
    else:
        try:
            model = json.loads(model)
        except:
            print("model not a valid Json")
            return None
    m = float(model['m'])
    c = float(model['c'])
    y = m * num + c
    return y