import pandas as pd
import math

dataframe = pd.read_csv("w09water.csv")

meterColumn = dataframe["meterSize"]\

filteredDataframe = dataframe[dataframe["meterSize"] < .8]

print(filteredDataframe)