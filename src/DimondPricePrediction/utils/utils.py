import os
import sys
import pickle
import numpy as np
import pandas as pd


sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction")

import logger

from exception import Customexception

from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise Customexception(e, sys)