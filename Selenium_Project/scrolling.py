import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1.) Scroll down the page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")



#2.) Scroll down the page till element found
#element = driver.find_element(By.XPATH, "//*[@id='HTML1']/div[1]/table/tbody/tr[2]/td[1]")
#driver.execute_script("arguments[0].scrollIntoView();", element)


#3.) Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)