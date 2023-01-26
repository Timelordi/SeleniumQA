import unittest

class SignupTest(unittest.TestCase):
        def test_signEmail(self):
            print("This is sign Email test")
            self.assertTrue(True)

        def test_singbyFacebook(self):
            print("This is sign by Facebook test")
            self.assertTrue(True)

        def test_signbyTwitter(self):
            print("This is sign by Twitter test")
            self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()