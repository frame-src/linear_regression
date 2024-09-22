from core.utils.signals_handler import signal_handler
from core.evaluation.execution import evaluate_model
from core.utils.header import HEADER_EVAL as HEADER
from core.utils.error_handler import error_message


import json


def main():
    print(HEADER)
    model_name = ("Please insert the MODEL_NAME of the model you want to evaluate: ")
    mse, mae = evaluate_model()
    print(" _______________________________")
    print("| MSE     | " + str(mse))
    print("|_________|_____________________")
    print("| MAE     | " + str(mae))
    print("_______________________________")


if __name__ == "__main__":
    signal_handler()
    main()
    if error_message:
        print(f"An error occurred: \n {error_message}")
    