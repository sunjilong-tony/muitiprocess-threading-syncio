# coding= utf-8
import time
from multiprocessing import Process
"""
multiprocessing
1.跨平台的多进程模块
2.提供了一个process类代表一个进程的对象
"""

# def run(name,des):
#     while 1:
#         print("**************** %s is %s" % (name, des))
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     # 创建进程（子进程，程序启动的进程称为主进程/父进程）target 接函数名，args接参数
#     p = Process(target=run, args=("tony", "good"))
#     # 启动子进程
#     p.start()
#
#     while 1:
#         print("/" * 20)
#         time.sleep(1.2)
import os
import time
from multiprocessing import Process


class Myprocess(Process):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def run(self):
        print("这个人的ID号是:%s" % os.getpid())
        print("这个人的名字是:%s" % self.name)
        time.sleep(3)


if __name__ == '__main__':
    p=Myprocess('李华')

    p.daemon=True       # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    # time.sleep(1) # 在sleep时linux下查看进程id对应的进程ps -ef|grep id
    print('主进程执行完毕!')
