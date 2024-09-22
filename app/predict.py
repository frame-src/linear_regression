from core.utils.signals_handler import signal_handler
from core.prediction.execution import make_prediction
import json


def main():
    num : float = 0
    question = "Please insert the model_name of the model you want to use: "
    model_name = None
    independent_value = 0

    while True:    
        if model_name == None:
            model_name = str(input(question))
        try: 
            independent_value = float(input("Please insert the value for the dependent_variable: "))
        except:
            print("Take care of inserting only valid number")
        predicted_value, label = make_prediction((independent_value), model_name)
        if predicted_value is None:
            model_name = None
            question = "Please insert a valid model Model_Name: "
        else:
            print(label + " = " + str(independent_value) + " " + str(type(independent_value)))
            print("\nThe expected value is: " + str(predicted_value))


if __name__ == "__main__":
    signal_handler()
    main()
    