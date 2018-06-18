import openpyxl

wb = openpyxl.Workbook()
print(wb)

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet')
print(sheet)

print(sheet['A1'].value)

print(sheet['A1'].value == None)

sheet['A1'] = 42


sheet['A2'] = 'Hello'
import os
os.chdir('/Users/Username/Downloads/')
wb.save('nkdemo.xlsx')

sheet2 = wb.create_sheet('sheet_nitesh')

print(wb.get_sheet_names())

print(sheet2.title)

sheet2.title = 'nk'
print(wb.get_sheet_names())

wb.save('example2.xlsx')