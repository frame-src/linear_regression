from core.training.execution import execute as train_model
from core.utils.fileio import save_model
from core.utils.header import HEADER
import json 

def main():
    print(HEADER)
    dataset_name = input( "Enter a dataset name (if none then a DEFAULT will be used): " )
    if not dataset_name :
        print("Running with default dataset...")
        m, c = train_model()
    else:
        print("Running with " + str(dataset_name))
        m, c = train_model(dataset_name)

    model_name = input("Enter a name for the model: ")
    path = save_model(m, c, model_name)
    if path:
        print("Model correctly saved at: " + (path))
    else : 
        print("Model not correctly saved; Please try again.")
    print(" To continue please train another model, or run the prediction script... Ciao")


if __name__ == "__main__": 
    main()
