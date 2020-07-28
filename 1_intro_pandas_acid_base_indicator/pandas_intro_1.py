#!/usr/bin/python3.6
import pandas
import numpy
import matplotlib
from matplotlib import pyplot

# Create a pandas dataframe using the .csv file provided:
df = pandas.read_csv("Acid_base_indicators_table.csv", header=None)

# Add headers to the dataframe:
headers = ["Indicator Name", "pH start", "pH end", "pKa", "Low pH color", "High pH color"]
df.columns = headers

# Print the first five rows:
print(" First five rows:")
print("---------------------------")
print(df.head(5))
print(" ")

# Print the last five rows:
print(" Last five rows:")
print("---------------------------")
print(df.tail(5))
print(" ")

# Print columns
print("Names of variables/features in columns")
print("-------------------------------------")
print(df.columns)
print(" ")

# Return a Series with the data type of each column:
print("Data types of variables in each column/features:")
print("-----------------------------------------------------")
print(df.dtypes)
print(" ")

# Evaluate missing data:
print("Missing data in last 10 rows of dataframe:")
print("-------------------------------------------------------")
missing_data = df.isnull()
print(missing_data.tail(10))
print(" ")

# Count the number of missing values in each column:
print("Count missing values in each column:")
print("----------------------------------------")
for column in missing_data.columns.values.tolist():
    print (missing_data[column].value_counts())
    print(" ")

# Find the middle between pH start and pH end:
df["pH mid"] = (df["pH start"] + df["pH end"]) / 2

# Draw plot correlating pH mid and pKa where pKa is available

# Relationship should be linear because at the mid point
# [H+] = kind, and the range of color change is equally
# distributed around the mid point, to a first approximation.
# Because: Kind = [H+][Ind-]/[HInd], and [Ind-] = [HInd]
# at the point of the color change

# Because of this, we can substitute pka with pH mid where it
# is not available
# (Just for practice with pandas. Missing values should never
# be substituted !!!)

# Divide indicators by acidity into bins:
# (Should use pkainstead of pH mid)
bins = numpy.linspace(min(df["pH mid"]), max(df["pH mid"]), 4)
acidity = ["acidic", "neutral", "basic"]
df["pH mid - binned"] = pandas.cut(df["pH mid"], bins, labels=acidity, include_lowest=True)
print(" Indicators binned by pH")
print("---------------------------")
print(df[["pH mid","pH mid - binned"]])
print(" ")
print(" Bins count:")
print("---------------------------")
print(df["pH mid - binned"].value_counts())
print(" ")

# Plot bins as histogram:
matplotlib.pyplot.figure('Histogram')
matplotlib.pyplot.xlabel("pH mid")
matplotlib.pyplot.ylabel("counts")
matplotlib.pyplot.title("pH mid binned")
matplotlib.pyplot.hist(df["pH mid - binned"], bins = 3)

# Plot bins as bar graph:
matplotlib.pyplot.figure('Bar Graph')
matplotlib.pyplot.xlabel("pH mid")
matplotlib.pyplot.ylabel("counts")
matplotlib.pyplot.title("pH mid binned")
matplotlib.pyplot.bar(df['pH mid - binned'].value_counts().index.tolist(), df["pH mid - binned"].value_counts())

matplotlib.pyplot.show()


