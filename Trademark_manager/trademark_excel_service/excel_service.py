# import os
# import openpyxl
#
# print("This is the excel service")
#
# # os.chdir('/home/psykinetic/workspace/Python_and_Django/Patent_Trademark_Manager/Trademark_manager/trademark_excel_service')
# wb = openpyxl.load_workbook('Instruction particulars.xlsx')
#
# print(wb.get_sheet_names())
# sheet = wb.get_sheet_by_name('Sheet1')
#
# for i in range(1,10) :
#     print( sheet.cell(row=1, column=i).value)
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
