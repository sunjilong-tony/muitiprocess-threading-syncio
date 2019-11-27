# coding= utf-8
'''
并发：指有多个任务需要同时进行
并行：同一时刻有多个任务执行
'''
import time
import asyncio

async def run(x):
    print('waiting:%d' % x)
    # 调用了一个耗时的操作
    await asyncio.sleep(x)
    return "done %d" % x

start = time.time()

corountine1 = run(2)
corountine2= run(3)
corountine3 = run(4)
corountine4= run(5)

tasks = [asyncio.ensure_future(corountine1), asyncio.ensure_future(corountine2)
        , asyncio.ensure_future(corountine3), asyncio.ensure_future(corountine4)]
loop = asyncio.get_event_loop()
# # 第一种
# loop.run_until_complete(asyncio.wait((tasks)))
# 第二种
loop.run_until_complete(asyncio.gather(*tasks))
for task in tasks:
    print("task返回值", task.result())
end = time.time()
print("time", end-start)