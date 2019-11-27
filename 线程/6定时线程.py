# coding= utf-8
import time
import threading

def run():
    print("12345")


if __name__ == '__main__':
    #进程启动后，不会阻塞主线程
    th = threading.Timer(5, run)
    th.start()
    th.join()

