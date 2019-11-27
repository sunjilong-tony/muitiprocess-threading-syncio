# coding= utf-8
import queue
import time
import threading
import random
# 线程条件变量
cond = threading.Condition()
'''
condition像Lock和Event的综合体，除基本的锁操作外，还提供了类似yield的功能。
在获取锁以后，可以调用wait()临时让出锁，当前线程被阻塞，
直到notify()发送通知后再次请求锁来恢复执行。将wait当做yield，那么notify就是send
'''
def run1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name+"----",i)
            time.sleep(1)
            cond.wait()
            cond.notify()
def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name+"----",i)
            time.sleep(1)
            # 释放
            cond.notify()
            cond.wait()
if __name__ == '__main__':
    arr = []
    th1 = threading.Thread(target=run1, name="th1")
    th1.start()
    th2 = threading.Thread(target=run2, name="th2")
    th2.start()
    th1.join()
    th2.join()
    print("end")