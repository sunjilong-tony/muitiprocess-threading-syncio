# coding= utf-8
"""
有名管道
无名管道
队列
共享内存
信号
信号量
"""
from multiprocessing import Queue, Process
import os
import time
import random

# q = Queue([maxsize])
# 创建共享的进程队列. maxsize是队列中允许的最大项数. 如果省略此参数, 则无大小限制. 底层队列使用管道和锁定实现. 另外, 还需要运行支持线程以便队列中的数据传输到底层管道中.
#
# # Queue的实例q具有以下方法:
#
# q.get([block[,timeout]])
# 返回q中的一个项目. 如果q为空, 此方法将阻塞, 直到队列中有项目可用为止. block用于控制阻塞行为, 默认为True, 如果设置为False, 将引发Queue.Empty异常(定义在Queue模块中). timeout是可选超时时间, 用在阻塞模式中, 如果在制定的时间间隔内没有项目变为可用, 将引发Queue.Empty异常.
#
# q.get_nowait()
# 同q.get(False)方法.
#
# q.put(item[,block[,timeout]])
# 将item放入队列. 如果队列已满, 此方法将阻塞至有空间可用为止. block控制阻塞行为, 默认为True. 如果设置为False, 将引发Queue.Empty异常(定义在Queue库模块中). timeout指定在阻塞模式中等待可用空间的时间长短, 超时后将引发Queue.Full异常.
#
# q.qsize()
# 返回队列中目前项目的正确数量. 此函数的结果并不可靠, 因为在返回结果和在稍后程序中使用结果之间, 队列中可能添加或删除了项目. 在某些系统上,
# 此方法可能引发NotImplementedError异常.
#
#
# q.empty()
# 如果调用此方法时q为空, 返回True. 如果其他进程或线程正在往队列中添加项目, 结果是不可靠的. 也就是说, 在返回和使用结果之间, 队列中可能已经加入新的项目.
#
# q.full()
# 如果q已满, 返回为True. 由于线程的存在, 结果也可能是不可靠的(参考q.empty()方法).


def produce(q):
    print("启动produce进程....")
    for i in range(5):
        print('将数据放在列表%s' % i)
        q.put(i)
        time.sleep(5)
    print("结束produce进程....")
def customer(q):
    print("启动customer进程...")
    while 1:
        print('等待数据')
        i = q.get(True)
        print("customer 数据%s" % i)
    print("结束")  # 不会执行，因强行结束


if __name__ == '__main__':
    q = Queue()
    pro = Process(target=produce, args=(q,))
    cus = Process(target=customer, args=(q,))
    pro.start()
    cus.start()
    pro.join()
    #cus 进程里是死循环，无法等待结束，只能强制结束子进程
    cus.terminate()
    print("结束")