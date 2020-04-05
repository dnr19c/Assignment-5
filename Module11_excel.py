import pandas as pd
from matplotlib import pyplot as plt


def get_frame():
    return pd.read_excel('C:/Users/danie/OneDrive/Documents/Datasets/COVID19.xlsx', index_col=None)
df = get_frame()
print(df)

data = df
data

My_County = data[data.COUNTYNAME == 'HILLSBOROUGH']
My_County

