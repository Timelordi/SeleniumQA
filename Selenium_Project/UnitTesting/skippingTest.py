import unittest

class AppTesting(unittest.TestCase):

    @unittest.skip #decorator
    def test_search(self):
        print("This is search test")

    def test_addvanced_search(self):
        print("This is advanced search method")

    def test_prepaid_search(self):
        print("This is test prepaid search test")

    def test_postpaid_search(self):
         print("This is test postpaid search test")

    def test_login_by_Gmail(self):
        print("This is Login By Email test")

    def test_login_by_Twitter(self):
        print("This is login by Twitter account")

if __name__== "__name__":
    unittest.main