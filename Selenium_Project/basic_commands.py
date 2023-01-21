import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")


driver.get("https://www.webometrics.info/")

driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/ul/li[4]/a").click()

time.sleep((5))

#driver.close()
driver.quit()