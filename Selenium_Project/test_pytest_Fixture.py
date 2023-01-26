import pytest

# To run the code in terminal: $pytest -v -s [test_file_name.py]
@pytest.fixture() #this allow us to select the before method
def setup():
    print("Once before every method")

def test_method1(setup): #setup runs before the mehtos execution
    print("This is test method 1")

def test_method2(setup): #setup runs before the mehtos execution
    print("This is test method 2")

