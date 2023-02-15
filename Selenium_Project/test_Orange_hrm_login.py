import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class OrangeHRM_test(unittest.TestCase):

#this is a beforehand class
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homepageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not mathing")

#this is an aftermath class
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Testing completed...")

if __name__ == "__name__":
    unittest.main()

    ##To run the test with HTML report: $pytest -v -s --html=report.html test_Orange_hrm_login.py
