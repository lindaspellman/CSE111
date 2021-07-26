import pandas as pd

dataframe = pd.read_csv("w09water.csv") 

print(dataframe.dtypes)

print(dataframe.describe())

meter_column = dataframe["meterSize"]

filtered_dataframe = dataframe[dataframe["meterSize"] < .8]

print(filtered_dataframe)