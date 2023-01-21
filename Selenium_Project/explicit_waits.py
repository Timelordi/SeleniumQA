import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.skyscanner.com/")
time.sleep(20)
driver.find_element(By.XPATH, "//*[@id='airli']/span").click()
time.sleep(3)

origin = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[1]/div/div/div/div/div/form/div[2]/div[1]/div[1]/div/div/input").send_keys("United States (US)")
time.sleep(2)
destination = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[1]/div/div/div/div/div/form/div[2]/div[1]/div[3]/div/div/input").send_keys('Cancun (CUN)')

dep_date = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[1]/div/div/div/div/div/form/div[2]/div[2]/div/div[1]/button/span").click()
time.sleep(2)
exact_dep_data = driver.find_element(By.XPATH, "/html/body/div[7]/section/div/div/div[2]/div/table/tbody/tr[1]/td[6]/button/span").click()

return_date = driver.find_element(By.XPATH,"/html/body/div[2]/main/div[1]/div/div/div[1]/div/div/div/div/div/form/div[2]/div[2]/div/div[2]/button/span").click()
time.sleep(2)
exact_ret_date = driver.find_element(By.XPATH, "/html/body/div[7]/section/div/div/div[2]/div/table/tbody/tr[2]/td[7]/button/span").click()

#click on submit
submit = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[1]/div/div/div/div/div/form/div[3]/button").click()

#Explicit waits
wait = WebDriverWait(driver,10)
element=wait.untill(EC.element_to_be_clickablelickable(By.XPATH, "Expected conditions"))
element.click()
time.sleep(3)

driver.quit()