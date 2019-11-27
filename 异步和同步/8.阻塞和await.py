# coding= utf-8
import time
import asyncio
'''
async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就向生成器的yield一样
函数交出控制权，协程遇到await，事件循环将会挂起该协程，执行其他的协程。直到其他协程也
挂起或执行完毕，再进行下一个协程的操作。
'''

async def run(x):
    print('waiting:%d' % x)
    # 调用了一个耗时的操作
    await asyncio.sleep(x)



start = time.time()

corountine = run(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(corountine)

loop.run_until_complete(task)

end = time.time()
print("time", end-start)