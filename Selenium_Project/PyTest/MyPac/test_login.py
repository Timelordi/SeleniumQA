import pytest
@pytest.yield_fixture()
def setup():
    print("\nOpen URL for Login")
    yield
    print("Closing browser after Login")
def test_loginByEmail(setup):
    print("This is Login by Email")

def test_loginByFacebook(setup):
    print("This is Login by Facebook")
