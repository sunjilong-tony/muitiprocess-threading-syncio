# coding= utf-8
import time
import random
import threading
# 创建全局threadlocal对象
#他能作为每个线程独立的存储空间
#每个线程对他都可以读写属性操作，但是互不影响
local = threading.local()
money = 0
def change(x, n):

    x += n
    x -= n
def run1(num):
    print(money)
    time.sleep(1)
    local.money = 2
    print("1--------%s" % local.money)
def run2(num):
    time.sleep(2)
    local.money = 3
    # for i in range(100000):
    #    change(num)
    print("2--------%s" % local.money)
if __name__ == '__main__':
    th1 = threading.Thread(target=run1, args=(5,), name="th1")
    th2 = threading.Thread(target=run2, args=(8,), name="th2")
    th1.start()
    th2.start()
    th1.join()
    th2.join()
