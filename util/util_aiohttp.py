import asyncio

import aiohttp
from log.logpro import log
from aiohttp import ClientSession


class AiohttpHandler:
    def __init__(self, ulr_list, max_thread=None):
        self.ulr_list = ulr_list
        # self.max_thread = max_thread

    # 发送请求
    async def fetch_get(self, url, method=None):
        async with ClientSession() as session:
            async with session.get(url) as response:
                return await response.read()

    # async def run(self, loop, r):
    #     url = 'http://127.0.0.1:8080/bankquota'
    #     tasks = []
    #     for i in range(r):
    #         task = asyncio.ensure_future(self.fetch(url))
    #         tasks.append(task)
    #         # 异步收集响应结果
    #         responses = await asyncio.gather(*tasks)
    #     print(responses)
    async def handle_tasks(self, work_queue, method):
        if method.lower() == 'get':
            while not work_queue.empty():
                current_url = await work_queue.get()
                try:
                    print(await self.fetch_get(current_url))
                except Exception as e:
                    print(e)
        if method.lower() == 'post':
            while not work_queue.empty():
                current_url = await work_queue.get()
                try:
                    print(await self.fetch_get(current_url))
                except Exception as e:
                    print(e)




    # loop = asyncio.get_event_loop()
    # future = asyncio.ensure_future(AiohttpHandler().run(loop, 5))
    # loop.run_until_complete(future)

    def eventloop(self):
        # 协程队列
        q = asyncio.Queue()
        # 遍历url加入队列
        [q.put_nowait(url) for url in self.ulr_list]
        # 创建事件循环
        loop = asyncio.get_event_loop()


        #任务列表
        tasks = [self.handle_tasks(q, 'post') ]
        # 将协程注册到事件循环，并启动事件循环
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()


if __name__ == '__main__':
    AiohttpHandler(['http://127.0.0.1:8080/bankquota' for i in range(5)]).eventloop()
