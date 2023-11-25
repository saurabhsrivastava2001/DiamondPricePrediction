import sys
import os
import pandas as pd
sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction")
import logger 

from exception import Customexception

sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction\\utils")

from utils.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts", "preprocessor.pkl")
            model_path=os.path.join("artifacts", "model.pkl")
            
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            return pred
            
            
            
            
        except Exception as e:
            raise Customexception(e,sys)

class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logger.logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logger.logging.info('Exception Occured in prediction pipeline')
            raise Customexception(e,sys)