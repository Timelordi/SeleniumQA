import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://dealtoday.com.mt/login/")

login_field = driver.find_element("name", "username")
print(login_field.is_displayed())
print(login_field.is_enabled())
login_field.send_keys("timelord_v_1.0@mail.ru")

passw= driver.find_element("name", "password")
print(passw.is_enabled())
print(passw.is_displayed())
passw.send_keys("Qwerty12")

sign_button = driver.find_element("name", "button")
sign_button.click()

After_login_element = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/div/div[2]/ul/li[5]/a")
print("This is the final statement:", After_login_element.is_displayed())
