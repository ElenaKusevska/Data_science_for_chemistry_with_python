#!/usr/bin/python3.6
import pandas
import numpy
import matplotlib
from matplotlib import pyplot

# Create a pandas dataframe using the .csv file provided:
df1 = pandas.read_csv("Mn_containing_catalysts_edited.csv", sep='|', encoding='utf_8')
df2 = pandas.read_csv("NO_cat_sum.csv", sep='|', encoding='utf_8')

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

# Print information on the columns by position
#print(df1.iloc[:, [0,1,2,3]].head(5))
#print(df1.iloc[:, [4,5,6]].head(5))
#print(df1.iloc[:, [7,8,9,10]].head(5))

# Print information about the columns
#print(df1.iloc[:, [0,1,2,3]].describe())
#print(df1.iloc[:, [4,5,6]].describe())
#print(df1.iloc[:, [7,8,9]].describe())


# What is the minimum T for a given NOx conversion?
df1['T2_av'] = df1['T2']
# Access all the elements in one column:
for i in range(0,len(df1)):
    a_str = df1.iloc[i,8]
    if ('-' in a_str):
        b_str = a_str.split('-')
        c_f = float(b_str[1]) #(float(b_str[1]) + float(b_str[0])) / 2.0
    else:
        c_f = float(a_str)
    print(c_f)
    df1.iloc[i,11] = c_f
df1['T2_av'] = df1['T2_av'].astype(float)
print(df1.iloc[:, [7,11]])

df1 = df1.rename(columns={'NOx conversion 2 - after introducing SO2 and/or H2O for a specified time': 'NOx conversion 2'})

print(" ")
print("group by - minimum T for given NOx conversion:")
print("----------------------------------------------------------")
df1_grp = df1.groupby('NOx conversion 2')['T2_av'].min()
print(df1_grp)

print(" ")
print("df1['Preparation process'].value_counts()")
print("---------------------------------------------")
print(df1['Preparation process'].value_counts())
