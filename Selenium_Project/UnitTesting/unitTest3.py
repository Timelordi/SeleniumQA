import unittest

class AppTesting(unittest.TestCase):
#setUp метод будет выполняться перед каждой нижестоящей функцией
    @classmethod
    def setUp(self): #этот метод выполняется каждый раз ПЕРЕД вызовом другого метода из этого класса
        print("This is login test")

    @classmethod
    def tearDown(self):#этот метод выполняется каждый раз ПОСЛЕ вызовом другого метода из этого класса
        print("This is logout test")

    @classmethod
    def setUpClass(cls):# #этот метод выполняется ЕДИНОЖДЫ ВНАЧАЛЕ
        print("Open application")

    @classmethod
    def tearDownClass(cls):  # #этот метод выполняется ЕДИНОЖДЫ В КОНЦЕ
        print("Close application")

    def test_search(self):
        print("This is a search test")

    def test_postpaid_search(self):
        print("This is a Postpaid search test")

    def test_advance_search(self):
        print("This is an advance search test")

    def test_prepaid_search(self):
        print("This is a Prepaid search test")

if __name__ == "__main__":
     unittest.main()