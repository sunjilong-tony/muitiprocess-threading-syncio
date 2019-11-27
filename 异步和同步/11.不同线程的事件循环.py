# coding= utf-8
'''
#一般情况我们的事件循环用于注册协程，有一些协程需要动态的添加到事件
循环汇总简单的方式就是使用多线程，当前线程创建一个事件循环，然后开启一个新
线程，在新县城中启动事件循环，那么当前线程不会被block
'''
import asyncio
import time
import threading
import multiprocessing

def start_loop(lp):
    # 启动事件循环
    asyncio.set_event_loop(lp)
    lp.run_forever()
def run(x):
    print('waiting:%d' % x)
    time.sleep(x)
    print( "done %d" % x)
start = time.time()


loop = asyncio.get_event_loop()
# 创建新线程，用于启动事件循环，此时不会阻塞主线程了

threading.Thread(target=start_loop,args=(loop,)).start()

end = time.time()
print("time", end-start)

# 给事件循环添加任务
loop.call_soon_threadsafe(run,4)

loop.call_soon_threadsafe(run,6)