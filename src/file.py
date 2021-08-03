#Class Imports:

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/water_potability.csv")

#Class Info:

print(df.info())
print(df.shape)
print(df.head())


#Class Cleaning:
print(df["Potability"].value_counts())
print(df.isna().sum())
df["Potability"] = df["Potability"].astype("category")
print(df.info())
#Class Visualisation:


#Class MachineLearning:
#Preprocessing
#Training
#Predict

