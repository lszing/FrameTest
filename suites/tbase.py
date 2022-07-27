import pytest

from log.logpro import log
from lib.common.case_control import Case_control
from abc import ABCMeta, abstractmethod
import sys

indent = '\n==============================================\n'


class TBase():
    case_data = {}
    def setup(self):
        log.info(f'{indent}开始执行用例')
        print('\n \033[4;33m 开始执行用例，并打印日志\033[0m')
        print(f'\nlogid is {log.logid}')

    def teardown(self):
        log.info("用例执行结束")
        print(f'\n用例执行结束{indent}')



    def test_scene_work(self, data):
        # 直接传全部数据 在caseControl中
        if 'info' in data:
            print(f"start! caseinfo is [{data['info']}]")
        Case_control(data).execute_control()
