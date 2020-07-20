#!/usr/bin/python3.6
import pandas

# Create a pandas dataframe using the .csv file provided:
df = pandas.read_csv("Acid_base_indicators_table.csv", header=None)

# Add headers to the dataframe:
headers = ["Indicator Name", "pH start", "pH end", "pKa", "Low pH color", "High pH color"]
df.columns = headers



print(df)
print(df.head(3))
