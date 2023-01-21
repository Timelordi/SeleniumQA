import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/bidi/log/package-summary.html")
time.sleep(3)

#Clickаем на первом IFrame выбирая элемент
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(2)
#возвращаемся на окно по умолчанию
driver.switch_to.default_content()


#Clickаем на втором IFrame выбирая элемент
driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(2)
#возвращаемся на окно по умолчанию
driver.switch_to.default_content()
time.sleep(2)

#Clickаем на третьем IFrame выбирая элемент
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()
