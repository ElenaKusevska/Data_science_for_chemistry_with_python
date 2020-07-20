#!/usr/bin/python3.6
import pandas

# Create a pandas dataframe using the .csv file provided:
df = pandas.read_csv("Acid_base_indicators_table.csv", header=None)

# Add headers to the dataframe:
headers = ["Indicator Name", "pH start", "pH end", "pKa", "Low pH color", "High pH color"]
df.columns = headers

# Print the first five rows:
print(df.head(5))

# Print the last five rows:
print(df.tail(5))

# Print columns
print(df.columns)

# Return a Series with the data type of each column:
print(df.dtypes)
