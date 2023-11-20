import os
import sys

sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction\\components")
from data_ingestion import DataIngestion

sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction")
import logger

from exception import Customexception
import pandas as pd


obj=DataIngestion()

obj.initiate_data_ingestion()