import unittest
from selenium import  webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.assertIsNone(driver) #драйвер пустой?
        self.assertIsNotNone(driver) #драйвер не пустой?


if __name__ == "__name__":
    unittest.main