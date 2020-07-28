#!/usr/bin/python3.6
import pandas
import numpy
import matplotlib
from matplotlib import pyplot

# Create a pandas dataframe using the .csv file provided:
#df1 = pandas.read_csv("Mn_containing_catalysts.csv", sep='|', encoding='utf_8')
df1 = pandas.read_csv("NO_cat_sum.csv", sep='|', encoding='utf_8')

# Print the first five rows:
print(" First three rows:")
print("---------------------------")
print(df1.head(3))
print(" ")

# Print the last five rows:
print(" Last three rows:")
print("---------------------------")
print(df1.tail(3))
print(" ")

# Print columns
print("Names of variables/features in columns")
print("-------------------------------------")
print(df1.columns)
print(" ")

# Return a Series with the data type of each column:
print("Data types of variables in each column/features:")
print("-----------------------------------------------------")
print(df1.dtypes)
print(" ")


