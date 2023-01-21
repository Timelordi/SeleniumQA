import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Timelord\PycharmProjects\Selenium_Project\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        title_of_web_page = driver.title
      #  self.assertEqual("Google", title_of_web_page, "Web page title is not the same") #оба должны совпадать
        self.assertNotEquals("Google", title_of_web_page) #оба должны отличаться
if __name__ == "__name__":
    unittest.main
