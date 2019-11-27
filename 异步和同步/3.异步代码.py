# coding= utf-8
import time
import asyncio

# 定义异步函数（定义一个协程）


async def func():
    # 模拟一个耗时io操作
    # asyncio.sleep(1)
    print("time%s" % time.time())


loop = asyncio.get_event_loop()
print(loop)
for i in range(5):
    loop.run_until_complete(func())