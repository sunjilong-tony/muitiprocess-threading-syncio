# coding= utf-8
from multiprocessing import Process, Pool
import os
import random
import time

def run(name):
    print("子进程启动 %s %d" % (name, os.getpid()))
    t1 = time.time()
    time.sleep(random.random() * 5)
    t2 = time.time()
    print("子进程结束 %s%d-%.2f" % (name, os.getpid(), t2-t1))


if __name__ == '__main__':
    print("启动主进程")
    # 进程池(如果不写值，默认系统的值)
    # 表示可以同时执行的进程数量
    # 由于pool的默认值为cpu的核心数量，如果有4个核心，则至少需要子进程才能看到等待的效果

    pool = Pool(4)
    for i in range(5):
        # 创建进程池放入进程中统一管理
        pool.apply_async(run, args=(i,))

    #进程池在调用join之前必须要调用close，调用close之后就不能向进程池中添加进程了
    pool.close()
    #pool 对象调用join方法，会等待所有子进程结束在执行主进程
    pool.join()

    print("结束主进程")