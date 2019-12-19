import os

print("This is the excel service")

# Read from excel sheet

# Create objects and populate with excel data

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

filename = ''
sheet_name = ''

df = pd.read_excel(filename, sheetname= sheet_name)

print("Column headings:")
print(df.columns)
