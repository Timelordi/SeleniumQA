import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest

class Test_Search(unittest.TestCase):
    def test_search(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        self.driver.find_element(By.XPATH,
                         "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(
    "Admin")
        self.driver.find_element(By.XPATH,
                         "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(
    "admin123")
        self.driver.find_element(By.XPATH,
                         "// *[ @ id = 'app'] / div[1] / div / div[1] / div / div[2] / div[2] / form / div[3] / button").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/input").click()
        action = ActionChains(self.driver)
        action.send_keys("D").send_keys("M").send_keys("I").send_keys("T").send_keys("R").send_keys("I").send_keys("Y").perform()
        time.sleep(10)

        search = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/input").is_selected()
        self.assertFalse(search)

if __name__ == "__name__":
        unittest.main


