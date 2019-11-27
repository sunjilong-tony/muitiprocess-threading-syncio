#! /usr/bin/python3
# coding= utf-8

# python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear.
#
# 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 wait 方法时就会阻塞，
# 如果“Flag”值为True，那么执行 wait 方法时便不再阻塞.
#
# is_set(): 查看一个事件的状态,默认为False
# clear(): 将“Flag”设置为False
# set(): 将“Flag”设置为True
"""
event 通过一个内部标记来协调多线程运行，方法wait（)阻塞线程执行，直到标记为True
set（）将标记为true，clear（）更改标记为flase，isSet()用于判断标记状态
如果不调用clear()，那么标记一直为True,wait()就不会发生堵塞行为。
通常为每个线程准备一个独立的Event，而不是多个线程共享，以避免未及时调用clear(0时发生意外情况。
"""


import time
from multiprocessing import Process, Event

# 创建一个"模拟红绿灯执行状态"的函数
def traffic_lights(e):
    while 1:
        print("!!!红灯亮!!!")
        time.sleep(5)
        e.set()     # 把e改为True
        print("~~~绿灯亮~~~")
        time.sleep(3)
        e.clear()   # 把e改为False

def car(i, e):
    if e.is_set() is False:  # 新来的车看到的是红灯,执行这里,车在等待
        print("车{}在等待......".format(i))
        e.wait()
        print("车{}走你........".format(i))
    else:               # 此时已经是绿灯,执行这里,车可以走了
        print("车{}可以走了....".format(i))

if __name__ == '__main__':
    e = Event()
    # 创建一个红绿灯
    tra_lig = Process(target=traffic_lights, args=(e,))
    tra_lig.start()
    while 1:
        time.sleep(1)
        # 创建3辆车
        for i in range(3):
            c = Process(target=car, args=(i, e))
            c.start()