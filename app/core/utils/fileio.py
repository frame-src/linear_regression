def extract_input_from_file (filename :str = "default_data.csv") -> list :
    PATH = "/usr/src/app/data/" + filename
    value = []
    try:
        with open(PATH) as f:
            for line in f:
                value.append(str(line))
        return value
    except:
        return None


def save_model(model:any = None, model_name :str = None ):
    PATH = "/usr/src/app/models/"
    if model_name is not None and model_name !=  "":
        PATH = PATH + model_name + ".txt"
    else:
        PATH = PATH + "model.txt"
    try:
        with open(PATH, 'a') as f:
            f.seek(0)
            f.write(model)
            f.truncate()
        return True
    except:
        return False


def load_model(model_name: str = None):
    if model_name is None:
        PATH = "/usr/src/app/models/model.txt"
    else :
        PATH = "/usr/src/app/models/" + str(model_name) + ".txt"
    try:
        with open(PATH) as f:
            for line in f:
                return line.replace("'", '"')
    except:
        return None
