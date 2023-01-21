from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.webometrics.info/")

print(driver.title)