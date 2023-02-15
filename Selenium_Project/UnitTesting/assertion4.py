#assertIN and assertNotIN
import unittest

class Test(unittest.TestCase):
    def testName(self):
     list={"python", "selenium", "java", "php"}

     self.assertIn("python", list) #слово python ожидается в списке list
     self.assertNotIn("python!", list) #слово python НЕ ожидается в списке list

if __name__ == "__name__":
    unittest.TestCase

