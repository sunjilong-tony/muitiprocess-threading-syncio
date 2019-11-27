# coding= utf-8
from multiprocessing import Process
from time import sleep


def run():
    print("启动子进程1")
    sleep(1)
    print("结束子进程1")

def run2():
    print("启动子进程2")
    sleep(1)
    print("结束子进程2")

if __name__ == '__main__':
    print("启动主进程")
    p = Process(target=run)
    p1 = Process(target=run2)
    p.start()
    p1.start()
    # 主进程结束不影响子进程，等待子进程结束，才能继续执行主进程
    # 主进程主要做的是调度相关的工作，不具体负责业务逻辑
    p.join()
    p1.join()
    print("结束主进程")

