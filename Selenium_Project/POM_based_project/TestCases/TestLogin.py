import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
import pytest
import LoginPage

sys.path.append("C://Users//Timelord//PycharmProjects//Selenium_Project\POM_based_project")

class LoginTest(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_Login(self):
        lp = LoginPage.LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)

        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__name__":
    unittest.main()
