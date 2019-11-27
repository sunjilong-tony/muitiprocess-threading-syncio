# coding= utf-8
'''
多线程和多进程最大的不同在于，多进程中，同一个全局变量，每个子进程各自有一份拷贝，互不影响
而在多线程中，所有的变量都由线程共享，所以任何一个变量都可以被任意线程锁修改
因此多个线程同时改变一个变量，容易把内容改乱了
'''
import time
import random
import threading
'''
模块
_thread低级点
threading 高级点 对_thread进行了分装
'''
money = 0
def change(n):
    global money
    money += n
    money -= n
def run1(num):
    time.sleep(3)
    print(money)
def run2(num):
    global money
    time.sleep(1)
    money = 100
if __name__ == '__main__':
    th1 = threading.Thread(target=run1, args=(1,), name="th1")
    th2 = threading.Thread(target=run2, args=(2,), name="th2")
    th1.start()
    th2.start()
