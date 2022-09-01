from pyasn1.debug import scope

from log.logpro import log
from lib.common.case_control import Case_control
from abc import ABCMeta, abstractmethod
import pytest
import sys

indent = '\n==============================================\n'


class TBaseNew:

    def setup(self):
        log.info(f'{indent}开始执行用例')
        print(f'\nlogid is {log.logid}')

    def teardown(self):
        log.info("用例执行结束")

    def test_scene_work(self, data):
        if 'info' in data:
            print(f"start! caseinfo is [{data['info']}]")
        Case_control(data).execute_control()
