#relational assertions
import unittest
from selenium import  webdriver

class Test(unittest.TestCase):
    def testName(self):
        #assertGreater
        self.assertGreater(int("6"), int("5"))
        self.assertLess(5, 6)
        self.assertGreaterEqual(6,6)
        self.assertLessEqual(6,6)

if __name__ == "__name__":
    unittest.main