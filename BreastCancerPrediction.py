# Importing required packages (numpy as np, pandas as pd, datasets from sklearn, matplotlib.pyplot as plt, )
import pandas as pd
import numpy as np                     # For mathematical calculations
import sklearn as sp
import matplotlib.pyplot as plt        # For plotting graphs
import seaborn as sns                  # For data visualization
%matplotlib inline
import warnings                        # To ignore any warnings warnings.filterwarnings("ignore")
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Reading data
df = pd.read_csv('C:/Users/ABC/Desktop/UWO M.Eng ECE Software Engg/02 Winter/9039B MACHINE LEARNING/Project/train_main.csv', header=0);

# Making copy of original data for backup
df_original = df.copy();

# Printing the dataset description
#print(df.describe())

# Checking the null values.
print(df.isnull().sum())

# Print data types for each variable
df.dtypes

# Exploratory Analysis

# Univariate Analysis
df['diagnosis'].value_counts()

# Normalize can be set to True to print proportions instead of number
df['diagnosis'].value_counts(normalize=True)

df['diagnosis'].value_counts().plot.bar()