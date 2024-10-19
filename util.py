import json
import pickle
import numpy as np
import sklearn   
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
     try:
         loc_index = __data_columns.index(location.lower())
     except:
         loc_index = -1
     x = np.zeros(len(__data_columns))
     x[0] = sqft
     x[1] = bath
     x[2] = bhk
     if loc_index >= 0:
         x[loc_index] = 1
     return round(__model.predict([x])[0],2) 
 
            
def get_location_names():
    return __locations

def load_saved_artifacts():
     print("loading saved artifacts___start")
     global __data_columns
     global __locations
     global __model
     with open("C:\\CODE\\Server\\artifacts\\columns.json", 'r') as f:
         __data_columns = json.load(f)['data_columns']
         __locations = __data_columns[5:]
     with open("C:\\CODE\\Server\\artifacts\\House_price_prediction.pickle", "rb") as f:
        __model = pickle.load(f)

     print("artifacts loaded")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Alandi Road',1000, 2, 2))
    print(get_estimated_price('Aundh',1000,2,2))
    