# coding= utf-8
import time


def func():
    time.sleep(1)


for i in range(5):
    func()
    print("time%s" % time.time())