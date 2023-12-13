import os
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import math

## import data
df = pd.read_csv('AAPL_dvae.csv', parse_dates=['Date'])
df = df.iloc[:, [0, 1, 2, 3, 4, 6]]  # Select columns by index


print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)


print(df.head())


df.to_csv("Finaldata_with_Fourier.csv", index=False)



