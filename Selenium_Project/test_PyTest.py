import time
import unittest
import _thread

from selenium import webdriver
import unittest

class Test(unittest.TestCase):
    def test_method1(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get('https://www.speedtest.net/')
        self.driver.maximize_window()



        self.assertEquals("Speedtest by Ookla - The Global Broadband Speed Test", driver.title)
        #assert driver.title == "Speedtest by Ookla - The Global Broadband Speed Test"


if __name__ == "__name__":
        unittest.main






