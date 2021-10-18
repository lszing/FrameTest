
import pytest


def sum(x, y):
    z = x + y
    return z

class Test():
    def test_1(self):
        print('afasdf')

    
if __name__ == '__main__':
    pytest.main(['-s','suites/test_example_testinherit.py','--alluredir','./temp'])