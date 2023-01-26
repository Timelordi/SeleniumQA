import pytest

import pytest
@pytest.yield_fixture()
def setup():
    print("\nOpen URL for Signup")
    yield
    print("\nClosing browser after Signup")
def test_SignByEmail(setup):
    print("This is SignUp by Email")

def test_SignByFacebook(setup):
    print("This is SignUp by Facebook")