from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/FileUpload.html")

driver.find_element(By.XPATH, "//*[@id='input-4']").send_keys("C:/Users/Timelord/Downloads/Agile interview questions.pdf")
time.sleep(3)