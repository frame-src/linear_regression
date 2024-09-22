from core.training.execution import train_model
from core.utils.fileio import save_model
from core.utils.header import HEADER
from core.utils.signals_handler import signal_handler
from core.utils.error_handler import error_message
import json 

def main():
    print(HEADER)
    dataset_name = input( "Enter a dataset name (if none then a DEFAULT will be used): " )
    dependent_variable_name = input ("Enter the dependent variable name: ")
    if not dataset_name :
        print("Running with default dataset                     ...")
        m, c = train_model(dependent_variable_name=dependent_variable_name)
    else:
        print("Running with " + str(dataset_name))
        m, c = train_model(dataset_name, dependent_variable_name)
    if not m: 
        print("An error occurred in Training")
    model_name = input("Enter a name for the model: ")
    path = save_model(m, c, dependent_variable_name, model_name)
    if path:
        print("Model correctly saved at: " + (path))
    else : 
        print("Model not correctly saved; Please try again.")
    print("\nPROCESS ENDED: To continue please train another model, or run the prediction script; \n")


if __name__ == "__main__":
    signal_handler() 
    if error_message:
        print(f"An error occurred: \n {error_message}")
    main()
