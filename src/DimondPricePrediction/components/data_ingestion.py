import pandas as pd
import numpy as np

import os

import sys
sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction")

import logger

from exception import Customexception

from sklearn.model_selection import train_test_split 

from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=("artifacts","train.scv")
    test_data_path:str=("artifacts","test.csv")
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logger.logging.info("data ingestion started ")
    
        try:
            data=pd.read_csv(Path(os.path.join("notebooks\data","train.csv")))
            logger.logging.info("I have read the dataset")
            
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logger.logging.info("I have save the raw data in the ARTIFACTS FOLDER")
        
            logger.logging.info("here I have perforemed train test split")
        
            train_data,test_data=train_test_split(data,test_size=0.25)
            logger.logging.info("train test split done")
            train_data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logger.logging.info("data ingestion completed")  
        
        except Exception as e:
            logger.logging.info("exception occured during data ingestion")
            raise Customexception(e,sys)