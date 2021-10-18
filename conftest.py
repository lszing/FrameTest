# content of conftest.py
import pytest
import random
from log.logpro import log
from util.readJson import ReadJson


def pytest_addoption(parser):
    parser.addoption(
        "--filter", action="store", default="default", help="my option: 1 or 2"
    )
    parser.addoption(
        "--path", action="store", default="", help="my option: 1 or 2"
        ,required=True
    )


# @pytest.fixture(scope="session")
# def data(request):
#     return request.config.getoption("--filter")


# @pytest.fixture(scope="session", autouse=True)
# def filter(request, cmdopt):
#     request.config.base_data = ReadJson().readJson(cmdopt)
#     return request.config.base_data


def pytest_generate_tests(metafunc):
    # 收集执行的测试方法的参数名称 即test(data)中的data
    # metafunc.config.getoption('--path')pytest参数--path
    # metafunc.config.getoption('--filter')pytest参数--filter
    if 'data' in metafunc.fixturenames:
        data = ReadJson(metafunc.config.getoption('--path'), filter=metafunc.config.getoption('--filter')).readJson()
        metafunc.parametrize('data', data)
