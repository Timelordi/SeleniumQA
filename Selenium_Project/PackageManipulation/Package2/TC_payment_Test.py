import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentInDollars(self):
        print("This is payment in Dollars")
        self.assertTrue(True)

    def test_paymentInEuro(self):
        print("This is payment in Euros")
        self.assertTrue(True)

if __name__ == "__name__":
    unittest.main()
