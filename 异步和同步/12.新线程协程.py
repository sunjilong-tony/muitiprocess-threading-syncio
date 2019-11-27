# coding= utf-8
import asyncio
import time
import threading
import multiprocessing

def start_loop(lp):
    # 启动事件循环
    asyncio.set_event_loop(lp)
    lp.run_forever()
async def run(x):
    print('waiting:%d' % x)
    await asyncio.sleep(x)
    print( "done %d" % x)
start = time.time()


loop = asyncio.get_event_loop()
# 创建新线程，用于启动事件循环，此时不会阻塞主线程了

threading.Thread(target=start_loop,args=(loop,)).start()



# 给事件循环添加任务
asyncio.run_coroutine_threadsafe(run(4), loop)
asyncio.run_coroutine_threadsafe(run(6), loop)
end = time.time()
print("time", end-start)