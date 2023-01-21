from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://www.webometrics.info/")

#Title of the page
print(driver.title)

#Return the URL of the load page
print(driver.current_url)

#Gives the HTML of the webpage
#print(driver.page_source)

driver.close() #close the browser