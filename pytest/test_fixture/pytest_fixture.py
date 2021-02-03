import pytest


def test_login1(login):
    print("登陆1：其他操作3")

def test_login2(login):
    print("登陆2：其他操作3")

def test_login3(login):
    print("登陆3：其他操作3")

if __name__ == "__main__":
    pytest.main('-s pytest_fixture.py')



