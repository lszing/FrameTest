# 启动top命令，把数据输入到文件top.log中
# 启动被测程序deamon,命令为deamon-t 3600 意思是运行3600秒后退出
# deamon标准输入全部丢弃 不打印到python程序的标准输出中，deamon的stderr写入文件error.log
# deamon结束时（可能正常结束，也可能异常退出）打印其exitcode 并停止top
import os, time
import subprocess
from typing import List

'''
subprocess.PIPE
一个可以被用于Popen的stdin 、stdout 和stderr 3个参数的特输值，表示需要创建一个新的管道。
subprocess.STDOUT
一个可以被用于Popen的stderr参数的输出值，表示子程序的标准错误汇合到标准输出。
'''

out = subprocess.Popen('deamon -t 3600', stderr=subprocess.PIPE)
lines = os.popen('top -bi -d 1').readlines()
for l in lines:
    with open('top.log', 'w', encoding='UTF-8') as f:
        f.write(l)
        f.write('\n')
stdout, stderr = out.communicate()
exitcode = out.returncode
for i in stderr:
    with open('error.log', 'w', encoding='UTF-8') as f:
        f.write(i)
        f.write('\n')

