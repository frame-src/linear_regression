from core.utils.signals_handler import handler
from core.evaluation.execution import make_prediction
import json


def main():
    num : float = 0
    question = "Please insert the model_name of the model you want to use: "
    model_name = None
    
    while True:    
        if model_name == None:
            model_name = str(input(question))
        try: 
            num = float(input("Please insert the KM of your car: "))
        except:
            print("Take care of inserting only valid number")
        price = make_prediction((num), model_name)
        if price is None:
            model_name = None
            question = "Please insert a valid model Model_Name: "
        else:
            print("KM = " + str(num) + " " + str(type(num)))
            print("The expected value is: " + str(price))


if __name__ == "__main__":
    main()
    