import selenium
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Windows.html")

action = ActionChains(driver)

interaction = driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/a")
dragNdrop = driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
static = driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a")

action.move_to_element(interaction).move_to_element(dragNdrop).move_to_element(static).click().perform()
driver.get("https://demo.automationtesting.in/Dynamic.html ")
driver.maximize_window()

target = driver.find_element(By.ID, "angular")
destination = driver.find_element(By.ID, "droparea")

action.drag_and_drop(target, destination).perform()