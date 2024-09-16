from core.header import HEADER
from core.training.execution import execute as train_model
from core.utils.fileio import save_model
import json 

def main():
    print(HEADER)
    dataset_name = input( "Enter a dataset name (if none then a DEFAULT will be used): " )
    if not dataset_name :
        print("Running with default data...")
        m, c = train_model()
    else:
        print("Running with " + str(dataset_name))
        m, c = train_model(dataset_name)
    model = {
            "m": m,
            "c": c
            }
    model_name = input("Enter a name for the model: ")
    save_model(json.dumps(model), model_name)

if __name__ == "__main__":
    main()
