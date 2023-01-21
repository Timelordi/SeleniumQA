import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import openpyexcel

path = r"C:\Users\Timelord\Downloads\Excel-To-Do-List-Template-Print.xlsx"
workbook = openpyexcel.load_workbook(path)
#выбрать если имеешь только 1 sheet в Excel документе
sheet = workbook.active #workbook.get_sheet_by_name("Sheet")

#посчитали количество строк и колонок
rows = sheet.max_row
columns = sheet.max_column
print(rows)
print(columns)

for r in range(1, rows+1):
    for c in range(1, columns+1):
        print(sheet.cell(row=r, column=c,).value, end=" ")
    print()