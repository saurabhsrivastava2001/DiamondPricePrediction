import sys
sys.path.append("C:\\Users\\SAURABH SRIVASTAVA\\Desktop\\firstENDTOEND\\src\\DimondPricePrediction\\pipelines")
from prediction_pipeline import CustomData

custom_data_object = CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data=custom_data_object.get_data_as_dataframe()

print(data)