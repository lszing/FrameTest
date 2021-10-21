import threading, time
import os
from queue import Queue

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/' + 'data' + '/'
# root 当前目录
# dirs 当前目录下所有子目录
# files 当前目录下所有非目录子文件
file_list = []
for root, dirs, files in os.walk(path):
    file_list = files
file_list_test = []
file_list_test.append(file_list[1].split('.')[0])
file_list_test.append(file_list[2].split('.')[0])
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
                # 判断任务队列为空跳过
                if self.work_queue.empty():
                    continue
                text = self.work_queue.get(block=True)
                os.system(f"pytest -v -s --path {text} {test_api_path}/test_api.py")
                self.work_queue.task_done()
            except Exception as e:
                print(f"thread-{self.getName()}: task is error : {str(e)}")
                break


class WorkManager:
    def __init__(self, thread_num):
        self.work_queue = Queue()  # 队列对象
        self.threads = []
        self._init_thread_pool(thread_num)

    # 初始化线程
    def _init_thread_pool(self, thread_num):
        for name in range(thread_num):
            # 将worker放入线程队列中
            self.threads.append(Worker(selfManage=self, name=str(name)))

    # 初始化工作队列 将任务放入当前类的任务队列中
    def add_job(self, job):
        self.work_queue.put(item=job)


def task(path):
    os.system(f"pytest -v -s --path {path} {test_api_path}/test_api.py")


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

    work_manager = WorkManager(1)
    for i in file_list_test:
        print(i)
        work_manager.add_job(i)
