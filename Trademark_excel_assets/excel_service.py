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
# import inspect
# import pandas as pd
# from pandas import ExcelWriter
# from pandas import ExcelFile


# postponing the upload feature in favour of making the app functional first
#
# def HelloService(obj):
#     # obj._meta.fields
#     property_list = [f.name for f in obj._meta.fields]
#     filename = '/home/psykinetic/workspace/Python_and_Django/Patent_Trademark_Manager/Trademark_excel_assets/Search.xlsx'
#     print("HelloService")
#     print("Column headings:")
#     df = pd.read_excel(filename, 'Sheet1')
#     print("PROPERTIES ",property_list, " length: ",property_list.__len__()," \n")
#     print("COLUMNS ",df.columns[0:property_list.__len__()],
#     " length: ", df.columns.__len__(), " \n")
#     count = 0
#     for i in df.index:
#         count+=1
#         # print("I think these are rows -->",df.index[i])
#         for j in df.columns:
#             # print("I think these are columns -->",df.columns)
#     print("finished counting -->", count)









# print("As if nested loops in python are a good fucking idea...")
# going by rows first
# for i in df.rows:
#     print(df.rows[i])
# for i in df.columns:
#     mySearchAction.
#     print(df.columns[i])
#     for j in df.index:
#         print(df[i][j])





    # clerk_searching,
    # conflicting_mark,
    # date_of_search_report,
    # date_reported_to_client,
    # official_search_fee,
    # reported_to_client,
    # search_instruction_date,
    # search_status,
    # search_type
    #
    #
    # clerk_searching = models.CharField(default="default value", max_length=50)
    # conflicting_mark = models.CharField(default="default value", max_length=50)
    # date_of_search_report = models.DateField()
    # date_reported_to_client = models.CharField(default="default value", max_length=50)
    # official_search_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    # reported_to_client = models.CharField(default="default value", max_length=50)
    # search_instruction_date = models.DateField()
    # search_status = models.CharField(default="default value", max_length=50)
    # search_type =  models.CharField(default="default value", max_length=50)
    #
    #




import csv
from xlrd import open_workbook

def HelloService(obj):
    print("HELLO SERVICE ACTIVATING")
#     filepath = '/home/psykinetic/workspace/Python_and_Django/Patent_Trademark_Manager/Trademark_excel_assets/Search.xlsx'
#     wb = open_workbook(filepath)
#     for sheet in wb.sheets():
#         number_of_rows = sheet.nrows
#         number_of_columns = sheet.ncols
#         items = []

#         rows = []
#         for row in range(1, number_of_rows):
#             values = []
#             for col in range(number_of_columns):
#                 value  = (sheet.cell(row,col).value)
#                 try:
#                     value = str(int(value))
#                 except ValueError:
#                     pass
#                 finally:
#                     values.append(value)
#             item = Arm(*values)
#             items.append(item)

#     for item in items:
#         print(item)
#         print("Accessing one single value (eg. DSPName): {0}".format(item.dsp_name))
#         print
#     # with open(filepath, newline='') as csvfile:
#     #     reader = csv.DictReader(csvfile)
#     #     for row in reader:
#     #         print(row)
