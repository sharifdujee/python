import numpy as np
import pandas as pd
print("Panda is ins")
import warnings
warnings.filterwarnings('ignore')
red_wine_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/Wine_Dataset/winequality-red.csv', sep=';')
#print(red_wine_data.head())
#print(red_wine_data.shape)
#print(red_wine_data.describe())
#print(red_wine_data['quality'].unique())
#print(red_wine_data['quality'].value_counts())

test_data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/exam_scores.csv', sep=',')
print(test_data.shape)
print(test_data.isnull().sum())
