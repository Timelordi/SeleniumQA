import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import openpyexcel

path = r"C:\Users\Timelord\Downloads\list.xlsx"
workbook = openpyexcel.load_workbook(path)
sheet = workbook.active

for r in range(1,11):
    for c in range(1,5):
        sheet.cell(row=r, column=c).value = "Welcome"

workbook.save(path)
