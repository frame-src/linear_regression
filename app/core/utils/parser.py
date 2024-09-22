from core.utils.fileio import extract_input_from_file

def split_line(string :str) :
    values = string.split(',')
    values[0] = float(values[0])
    values[1] = float(values[1])
    return values


def create_array_x_and_y(values: list):
    x = []
    y = []

    name_x = None
    for value in values:
        if name_x == None:
            name_x, name_y = str(values[0]).split(',')
            x.append(name_x)
            y.append(name_y)
        else :
            values = split_line(str(value))
            x.append(values[0])
            y.append(values[1])

    return x,y


def execute_parsing(dataset_name: str = "default_data.csv") :
    print("Executing parsing                                ...")
    content = extract_input_from_file(dataset_name)
    if content == None:
        return None, None
    return create_array_x_and_y(content)
