import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import XLutils

driver = webdriver.Chrome(executable_path=r"/chromedriver_win32/chromedriver.exe")
driver.get("https://www.sportsdirect.com/login")
#Ждем пока загрузится
time.sleep(3)
driver.maximize_window()

#Соглашаемся с Куки
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

#Закрываем страничку выбора страны
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/button").click()
time.sleep(3)

path = r"C:\Users\Timelord\Downloads\list.xlsx"

rows = XLutils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLutils.readData(path, "Sheet1", r, 1)
    password = XLutils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.XPATH, "//*[@id='Login_EmailAddress']").send_keys(username)
    driver.find_element(By.XPATH, "//*[@id='Login_Password']").send_keys(password)

    driver.find_element(By.XPATH, "//*[@id='LoginButton']").click()

    if driver.title == "SportsDirect.com – The UK’s No 1 Sports Retailer":
        print("Test is passed")
        XLutils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test Failed")
        XLutils.writeData(path, "Sheet1", r, 3, "Test Failed")
        time.sleep(6)
    driver.find_element(By.XPATH, "//*[@id='divSignIn']/a/span[1]").click()

#bupsopups@mail.ru
#Qwerty12