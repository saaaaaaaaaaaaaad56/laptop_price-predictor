from gettext import install

import pip




import pandas as pd
import numpy as np




df = pd.read_csv('C:/Users/muham/OneDrive/Desktop/laptop_price predictor/dataset.csv')
print(df.head())

print(" the number of duplicated rows are: ",df.duplicated().sum())
print(" the number of missing values are: ",df.isnull().sum().sum())




import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(df['Price'])
plt.show()


