# coding= utf-8
import threading
import time
import queue

'''
event 通过一个内部标记来协调多线程运行，方法wait（)阻塞线程执行，直到标记为True
set（）将标记为true，clear（）更改标记为flase，isSet()用于判断标记状态
如果不调用clear()，那么标记一直为True,wait()就不会发生堵塞行为。
通常为每个线程准备一个独立的Event，而不是多个线程共享，以避免未及时调用clear(0时发生意外情况。
'''
def func():
    event = threading.Event()
    def run():
        for i in range(10):
            # 阻塞
            # event.wait()
            # 重置
            # event.clear()
            print("-----------" +str(i))
    th = threading.Thread(target=run)
    th.start()
    return event
event = func()
for i in range(10):
    event.set()
    print(threading.current_thread().name)
    time.sleep(1)
print("End")
