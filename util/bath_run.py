import threading, time
import os
from queue import Queue

data_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'data' + '/'
temp_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'temp' + '/'
report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'report' + '/'
# root 当前目录
# dirs 当前目录下所有子目录
# files 当前目录下所有非目录子文件
file_list = []
for root, dirs, files in os.walk(data_path):
    file_list = files
file_list_test = []
for i in file_list:
    file_list_test.append(i.split('.')[0])
# file_list_test.append(file_list[7].split('.')[0])
test_api_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'suites'


class Worker(threading.Thread):
    def __init__(self, selfManage, name):
        threading.Thread.__init__(self)
        self.work_queue = selfManage.work_queue
        self.name = name
        self.start()

    def run(self):
        while True:
            try:
                # 判断任务队列为空结束死循环
                if self.work_queue.empty():
                    os.system(f"allure generate {temp_path} -o {report_path} --clean ")
                    break
                text = self.work_queue.get(block=True)
                os.system(f"pytest -v -s --path {text} --alluredir {temp_path} {test_api_path}/test_api.py")
                self.work_queue.task_done()
            except Exception as e:
                print(f"thread-{self.getName()}: task is error : {str(e)}")
                break


class WorkManager:
    def __init__(self, thread_num, job):
        self.work_queue = Queue()  # 队列对象
        self.threads = []
        self.add_job(job)
        self._init_thread_pool(thread_num)

    # 初始化线程
    def _init_thread_pool(self, thread_num):
        for name in range(thread_num):
            # 将worker放入线程队列中
            self.threads.append(Worker(selfManage=self, name=str(name)))

    # 初始化工作队列 将任务放入当前类的任务队列中
    def add_job(self, job_list):
        for i in job_list:
            self.work_queue.put(item=i)


def task(path):
    os.system(f"pytest -v -s --path {path} --alluredir ./temp {test_api_path}/test_api.py ")


def runthead():
    # pool = [1, 2,3]
    for i in file_list_test:
        print(i)
        a = threading.Thread(target=task, args=(i,))
        a.start()


if __name__ == '__main__':
    # runthead()
    # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(path)

    work_manager = WorkManager(1, file_list_test)
