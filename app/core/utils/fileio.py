import os
import json

def extract_input_from_file (filename :str = "default_data.csv") -> list :
    current_directory = str(os.getcwd())
    PATH = current_directory + "/data/" + filename
    value = []
    try:
        with open(PATH) as f:
            for line in f:
                value.append(str(line))
        return value
    except:
        return None


def save_model(m: float = 0, c : float = 0, model_name :str = None )-> str:
    current_directory = str(os.getcwd())
    PATH = current_directory + "/models/"
    model = {
                "m": m,
                "c": c
        }
    if model_name is not None and model_name !=  "":
        PATH = PATH + model_name + ".txt"
    else:
        PATH = PATH + "model.txt"
    try:
        with open(PATH, 'a') as f:
            f.seek(0)
            f.write(json.dumps(model))
            f.truncate()
    except:
        PATH = None
    return PATH



def load_model(model_name: str = None):
    current_directory = str(os.getcwd())
    if model_name is None:
        PATH = current_directory + "/models/model.txt"
    else :
        PATH = current_directory + "/models/" + str(model_name) + ".txt"
    try:
        with open(PATH) as f:
            for line in f:
                return line.replace("'", '"')
    except:
        return None
