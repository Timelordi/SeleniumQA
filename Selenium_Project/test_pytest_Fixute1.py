import pytest
@pytest.yield_fixture()
def setup():
    print("\nOnce before every method") # эта часть будет выполняться перед каждым методом
    yield # разделить того что будет ДО и ПОСЛЕ
    print("Once after every method") # эта часть будет выполняться после каждого метода
def test_method1(setup):
    print("This is a method 1")

def test_method2(setup):
    print("This is a method 2")