import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://www.webometrics.info/")

print(driver.title)

driver.get("http://ww7.demoaut.com/")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)

