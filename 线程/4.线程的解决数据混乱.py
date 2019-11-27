# coding= utf-8
'''
问题：两个线程同时一村一区，可能造成变量值不对，
保证一个线程在修改变量的时候，其他的线程一定不能修改
后期在线程中上锁，但是要注意释放锁（自己的锁自己放），否则会造成死锁
GIL锁查看看

'''
import time
import random
import threading

lock = threading.Lock()
money = 0
def change(n):
    global money
    money += n
    money -= n
def run1(num):
    for i in range(1000000):
        # 获取线程锁，如果以上锁，则阻塞等待锁的释放
        # 当多个线程同时执行lock.acquire()
        # 时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
        #
        # 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
        # 所以我们用try...finally来确保锁一定会被释放
        lock.acquire()
        try:
            change(num)
        finally:
            lock.release()
def run2(num):
   for i in range(100000):
       with lock:
            change(num)
if __name__ == '__main__':
    th1 = threading.Thread(target=run1, args=(5,), name="th1")
    th2 = threading.Thread(target=run2, args=(8,), name="th2")
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print("%d" % money)