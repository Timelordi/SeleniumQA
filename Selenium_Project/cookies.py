from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://amazon.com/")

#capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))

#adding new cookie to browser
cookie = {'name': "Value", 'value':"TestCookie"}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(cookies)
print(len(cookies)) # print number of cookies after manual adding new cookie

#delete cookies
#driver.delete_all_cookies() #remove all cookies
driver.delete_cookie("Value") #remove the cookie manually
cookies = driver.get_cookies() #NEED! to get new cookies for driver
print(len(cookies))
