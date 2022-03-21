# coding=utf-8
# content of conftest.py
import sys

import pytest
import random
from log.logpro import log
from util.json_util import ReadJson
import importlib


def pytest_addoption(parser):
    parser.addoption(
        "--filter", action="store", default="default", help="my option: 1 or 2"
    )
    # parser.addoption(
    #     "--path", action="store", default="", help="my option: 1 or 2"
    #     , required=True
    # )


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
        all_caseData = get_all_caseData(sys.argv)
        log.info(f'all case data={all_caseData}')
        data = handle_data(metafunc.config.getoption('--filter'), all_caseData)
        log.info(f'Filtered data={data}')
        # data = ReadJson(metafunc.config.getoption('--path'), filter=metafunc.config.getoption('--filter')).readJson()
        metafunc.parametrize('data', data)


def get_all_caseData(argv: list):
    path = argv[-1]
    if '\\' in path:
        filename = path.split('\\')[-1]
    elif '/' in path:
        filename = path.split('/')[-1]
    else:
        filename = path
    mod = importlib.import_module('suites.' + filename[:-3])
    classObj = getattr(mod, filename[:-3].capitalize())
    return classObj.case_data


def handle_data(filter, caseData):
    result = []
    if filter is None or filter == '' or filter == 'default':
        return [value for key, value in caseData.items()]
    try:
        result.append(caseData[filter])
    except:
        log.fatal(f'filter [{filter} not in caseData [{caseData}]]')
        raise Exception
    return result
