import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

#print(driver.current_window_handle) # CDwindow-9D1EEA74388F1ABFA03489F539E04D26     - Parent Window

handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()  #close the parent browser tab

time.sleep(5)
driver.quit()