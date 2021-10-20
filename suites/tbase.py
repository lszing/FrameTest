from log.logpro import log
from lib.common.case_control import Case_control
from abc import ABCMeta, abstractmethod


class TBase():

    def setup(self):
        log.info("开始执行用例")
        print('\n开始执行用例，并打印日志')

    def teardown(self):
        log.info("用例执行结束")
        print('\n用例执行结束')


    def test_scene_work(self, data):
        # 直接传全部数据 在caseControl中
        Case_control(data).execute_control()

