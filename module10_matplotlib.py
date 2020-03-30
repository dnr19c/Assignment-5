# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:40:18 2020

@author: danie
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:/Users/danie/OneDrive/Documents/Datasets/heart-disease-uci-heart.csv')
cols = ['age','trestbps','chol','thalach']

data = df.groupby(df['sex']=='1')[cols].head(5)
ix = np.arange(len(data))

bar_width = .25


plt.bar(ix, 'thalach', width=bar_width, data=data, color='g', label='Maximum Heart Rate Achieved ')
plt.bar(ix + bar_width, 'chol', width=bar_width, data=data, color='b', label='Cholesterol')
plt.bar(ix + bar_width*2, 'trestbps', width=bar_width, data=data, color='r', label='Blood Pressure')
plt.xticks(ix, data['age'])
plt.ylim(0,400)
plt.legend()
plt.show()
