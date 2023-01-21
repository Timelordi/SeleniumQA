from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://amazon.com/")

driver.save_screenshot(r'C:\Users\Timelord\Downloads\screenshot.jpeg')

driver.get_screenshot_as_file(r'C:\Users\Timelord\Downloads\screenshot1.jpeg')