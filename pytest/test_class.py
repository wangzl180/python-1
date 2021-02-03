import pytest

class TestClass:

    # def setup(self):
    #     print("setup：每个用例执行一次")
    #
    # def teardown(self):
    #     print("teardown：用例执行完毕")

    def test_one(self):
        # print("正在执行：one")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        # print("正在执行：two")
        x = '123'
        assert '12' in x

    def test_three(self):
        # print("正在执行：three")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main('-q test_class.py::TestClass::test_two')
    print("test")
