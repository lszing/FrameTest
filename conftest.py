# coding=utf-8
# content of conftest.py

import sys

import pytest
from py.xml import html
from _pytest.config import Config
from log.logpro import log
import importlib
import os

case_info = ''
case_path = ''
case_list = []
case_error_list = []

global_data = {}


def set_global_data(key, value):
    def _set_global_data(key, value):
        global_data[key] = value

    yield _set_global_data


def pytest_configure(config):
    # 删除ptest-html中的Java_Home和Plygins
    config._metadata.pop('JAVA_HOME')
    config._metadata.pop('Plugins')


def pytest_addoption(parser):
    parser.addoption(
        "--filter", action="store", default="default", help="case1 case2.."
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

# 钩子函数生成测试项
def pytest_generate_tests(metafunc):
    # 收集执行的测试方法的参数名称 即test(data)中的data
    # metafunc.config.getoption('--path')pytest参数--path
    # metafunc.config.getoption('--filter')pytest参数--filter
    if 'data' in metafunc.fixturenames:
        all_caseData = get_all_caseData(sys.argv)
        log.info(f'all case data={all_caseData}')
        data = handle_data(metafunc.config.getoption('--filter'), all_caseData)
        log.info(f'filtered data={data}')
        ids = ['info:{}'.format(i) for i in data]
        print(ids)
        # info = data[0]['info']
        # data = ReadJson(metafunc.config.getoption('--path'), filter=metafunc.config.getoption('--filter')).readJson()
        metafunc.parametrize('data', data)


def get_all_caseData(argv: list):
    global case_path
    path = argv[-1]
    filename = ''
    if path[-2:] != 'py':
        all_caseData = []
        class_obj_list = get_all_data_file()
        for i in class_obj_list:
            all_caseData.append(i.case_data)
        return all_caseData
    else:
        case_path = path
        if '\\' in path:
            filename = path.split('\\')[-1]
        elif '/' in path:
            filename = path.split('/')[-1]
        else:
            filename = path
    mod = importlib.import_module('suites.' + filename[:-3])
    class_obj = getattr(mod, filename[:-3].capitalize())
    # class_obj = getattr(mod, filename[:-3])
    return class_obj.case_data


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


def get_all_data_file():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    data_path = absolute_path + '/suites/'
    file_list = ''
    for root, dirs, files in os.walk(data_path):
        file_list = files
        break
    class_obj_list = []
    failed_file = []
    for fileName in file_list:
        splited_fileName = fileName.split('.')[0]
        if 'test' not in splited_fileName:
            continue
        try:
            mod = importlib.import_module('suites.' + splited_fileName)
            class_obj = getattr(mod, splited_fileName.capitalize())
            class_obj_list.append(class_obj)
        except Exception as e:
            log.fatal(f'error filename is [{splited_fileName}],Exception:[{e}]')
            failed_file.append(splited_fileName)
            continue
    print(failed_file)
    return class_obj_list


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    """
    　　每个测试用例执行后，制作测试报告
    　　:param item:测试用例对象
    　　:param call:测试用例的测试步骤
                先执行when=’setup’ 返回setup 的执行结果
                然后执行when=’call’ 返回call 的执行结果
                最后执行when=’teardown’返回teardown 的执行结果
    　　:return:
    　　"""
    out = yield
    # 获取调用结果的测试报告，返回一个report对象, report对象的属性包括when（steup, call, teardown三个值）、nodeid(测试用例的名字)、outcome(用例的执行结果，passed,failed)
    report = out.get_result()
    # 这个不能放在call中
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        case_result = report.outcome  # 用例执行结果
        case_dict = {'info': case_info, 'path': case_path, 'result': case_result}
        # 获取case信息插入到列表中
        # case_list.append(case_info)
        print(f'now is calling')
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure

            error_info = str(call.excinfo)[1:-1]
            print(f'error_info is {error_info}')
            print(f'error_info is {call}')
            extra.append(pytest_html.extras.html(f"<div class=\"fail log\">{error_info}</div>"))
        report.extra = extra

    # if report.when == 'teardown':
    #     断言失败信息
    #     print(f'call is {call}')
    #     print(f'call is {call.excinfo.value}')
    #     print(f'call is {call.excinfo.type}')
    #     print(f'call is {call.excinfo.typename}')
    #     print(f'call is {call.excinfo.exconly()}')
    #     print(f'call is {call.excinfo.traceback}')


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    pass


def pytest_make_parametrize_id(config: Config, val: object, argname: str):
    if 'info' in val.keys():
        case_list.append(val['info'])
        # case_info = val['info']
        print('=========================================={}'.format(case_list))


# def pytest_runtest_logreport(report):
#     print('=========================================={}'.format(report))


# def pytest_sessionfinish(session, exitstatus):
#     print(f'run status code:', exitstatus)
# passed_amount = sum(1 for result in session.results.values() if result.passed)
# failed_amount = sum(1 for result in session.results.values() if result.failed)
# print(f'there are {passed_amount} passed and {failed_amount} failed tests')


# pytest-html报告结果列表 增加列头'Description'
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    # 删除link列
    cells.pop()


# pytest-html报告结果列表 Description列增加具体数据   case运行最后生成报告前才执行n遍  n代表case数
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    print(case_list)
    cells.insert(1, html.td(case_list.pop(0)))
    # 删除link列
    cells.pop()


def pytest_html_results_table_html(report, data):
    if report.failed:
        # 删除log
        data.pop()
        # data.append(html.span(f'error_info', class_='fail log'))


if __name__ == '__main__':
    print(get_all_data_file())
