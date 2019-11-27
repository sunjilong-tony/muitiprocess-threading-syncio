# coding= utf-8
import time
import asyncio

async def run(x):
    print('waiting:%d' % x)

    await asyncio.sleep(x)
    return "done %d" % x

start = time.time()
async def main():
    corountine1 = run(2)
    corountine2= run(3)
    corountine3 = run(4)
    corountine4= run(5)
    tasks = [asyncio.ensure_future(corountine1),
                  asyncio.ensure_future(corountine2),
                  asyncio.ensure_future(corountine3),
                  asyncio.ensure_future(corountine4)]
    # 第一种
    # dones,pending = await asyncio.wait(tasks)
    # print("-----------------")
    # for task in tasks:
    #     print("taskf返回值",task.result())
    # 第二种
    # res = await asyncio.gather(*tasks)
    # for result in res:
    #     print("返回值",result)
    # 第三种
    return await asyncio.wait(tasks)
loop = asyncio.get_event_loop()
# 第一种
# loop.run_until_complete(main())
# 第二种
# loop.run_until_complete(main())
# 3
done,pending = loop.run_until_complete(main())
for task in done:
    print("返回值", task.result())
end = time.time()
print("time", end-start)