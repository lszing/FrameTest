import pytest
class Test_example:

    def test1(self,mysetup,mycasesetip):
        print(1)
    def test2(self,mysetup,mycasesetip):
        print(2)

    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def setup_class(self):
        print('class setup')

    def teardown_class(self):
        print('class teardown')

    #scope='module'相当于setup_class 但比setup先执行 其中yield区分setup和teardown
    @pytest.fixture(scope='module')
    def mysetup(self):
        print('module start')
        yield
        print('module end')
    #scope='function'相当于setup 但在setup执行前执行
    @pytest.fixture(scope='function')
    def mycasesetip(self):
        print('function start')
        yield
        print('function end')


if __name__ == '__main__':
    pytest.main(['-s','test_example.py'])
