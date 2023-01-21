from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

#Появилось всплывающее окно от браузера с ОК или Cancel
#Нажимаем ОК
#Alert(driver).accept()

#Или нажимаем Cancel
Alert(driver).dismiss()

time.sleep(3)