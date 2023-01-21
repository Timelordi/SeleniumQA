import unittest
from selenium import webdriver

class SearchEngines(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()

    def test_yahoo(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.yahoo.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()

if __name__ == 'main':
    unittest.main()
