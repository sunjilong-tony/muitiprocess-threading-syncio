# coding= utf-8
import queue
import time
import threading
import random


def produce(q, index):
    while 1:
        num = random.randint(0, 1000000)
        q.put("生产者%s产生的数据%d" % (index, num))
        print("生产者%s产生的数据%d" % (index, num))
        time.sleep(2)
    # 完成任务
    q.task_done()

def customer(q, index):
    while 1:
        item = q.get()
        if item is None:
            break
        print("消费者%s获取的数据%s" % (index, item))
    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []
    for i in range(3):
        th = threading.Thread(target=produce, args=(q, i))
        th.start()
        # th.join()
    for a in range(5):
        th = threading.Timer(10, customer, args=(q, a))
        th.start()
        arr.append(th)
    for th in arr:
        th.join()
    print("end")