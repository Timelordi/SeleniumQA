import time

import selenium
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class TestOrange():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepage_title(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        self.driver.find_element(By.XPATH, "// *[ @ id = 'app'] / div[1] / div / div[1] / div / div[2] / div[2] / form / div[3] / button").click()

        assert self.driver.title == "OrangeHRM"

#To generate report pytest -v -s --html=report.html --self-contained-html .\test_Orange_HRM.py
