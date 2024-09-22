from core.utils.signals_handler import signal_handler
from core.prediction.execution import make_prediction
from core.utils.header import HEADER_PREDICT as HEADER

import json


def main():
    num : float = 0
    print(HEADER)
    question = "Please insert the MODEL_NAME of the model you want to use: "
    model_name = None
    independent_value = 0
    while True:    
        if model_name == None:
            model_name = str(input(question))
        try: 
            independent_value = float(input("Please insert the value for the DEPENDENT_VARIABLE: "))
        except:
            print("Take care of inserting only valid number")
        print(independent_value)
        predicted_value, label = make_prediction((independent_value), model_name)
        if predicted_value is None:
            model_name = None
            question = "Please insert a valid MODEL_NAME: "
        else:
            print(label + " = " + str(independent_value) + " " + str(type(independent_value)))
            print("\nThe expected value is: " + str(predicted_value))


if __name__ == "__main__":
    signal_handler()
    main()
    if error_message:
        print(f"An error occurred: \n {error_message}")
    