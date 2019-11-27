# coding= utf-8
import time
import random
import threading
'''
模块
_thread低级点
threading 高级点 对_thread进行了分装
'''
def run1(num):
    print("启动%s子线程1---%s" % (threading.current_thread().name, num))
    time.sleep(random.random() * 5)
    print("结束%s子线程1---%s" % (threading.current_thread().name, num))

def run2(num):
    print("启动%s子线程2---%s" % (threading.current_thread().name, num))
    time.sleep(random.random() * 5)
    print("结束%s子线程2---%s" % (threading.current_thread().name, num))

if __name__ == '__main__':
    # threading.current_thread()获取当前线程对象
    # 主线程的名称默认为MainThread
    print("主线程启动%s" % threading.current_thread().name)
    # 创建线程name给线程取名字
    th1 = threading.Thread(target=run1, args=(1,), name="th1")
    th2 = threading.Thread(target=run2, args=(2,), name="th2")
    # 启动
    th1.start()
    th2.start()
    # 等待子线程结束
    th1.join()
    th2.join()
    print("主线程结束%s" % threading.current_thread())

