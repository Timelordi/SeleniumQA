import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        title = driver.title
        #self.assertTrue("Google" == title)
        self.assertFalse("Google" == title)


if __name__ == "__name__":
    unittest.main