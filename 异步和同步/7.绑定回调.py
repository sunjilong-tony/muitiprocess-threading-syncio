# coding= utf-8
import  time
import asyncio

async def run(x):
    print('waiting:%d'  % x)
    return "done %d" %x
# 定义个回调函数
def callback(future):
    print("callback",future.result())
start = time.time()
corountine = run(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(corountine)
# 给任务添加回调，在任务结束后调用回调函数
task.add_done_callback(callback)
loop.run_until_complete(task)

end = time.time()
print("time", end-start)