import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("file:///C:/Users/Timelord/Downloads/Table.html")

rows = len(driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/table/tbody/tr")) #count the number of rows
columns = len(driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/table/thead/tr/th")) #count the number of columns

print(rows)
print(columns)


for r in range(1, rows+1):
    for c in range(1, columns+1):
        value = driver.find_element(By.XPATH, "/ html / body / div / div / div / div / div[2] / div[1] / table / tbody / tr["+str(r)+"] / td["+str(c)+"]").text
        print(value, end="   ")
    print()


