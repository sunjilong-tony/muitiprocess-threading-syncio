# coding= utf-8
import time


def produce(c):
    c.send(None)
    for i in range(5):
        print("produce 生产数据%d" %i)
        res = c.send(str(i))
        print("produce消费者反馈%s" % res)
        time.sleep(2)
        # 关闭消费者
    c.close()


def customer():
    res = ""
    while True:
        data = yield res
        if not data:
            return
        print("customer消费数据%s" %data)
        res = "200 ok"

c = customer()
produce(c)