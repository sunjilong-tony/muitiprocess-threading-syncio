# coding= utf-8
import  time
import asyncio
import threading
import multiprocessing


# 通过async关键字定义了一个协程，协程不能直接运行，需要将协程加入到事件循环中
async def run(x):
    print('waiting:%d'  % x)
start = time.time()
# 得到一个协程对象，这个时候没有执行
corountine = run(2)
print(type(corountine))
# 创建一个时间循环(在模块中获取一个引用)
loop = asyncio.get_event_loop()
# 将协程对象加入到事件循环
loop.run_until_complete(corountine)
end = time.time()
print("time",end-start)