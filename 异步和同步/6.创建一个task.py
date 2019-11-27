# coding= utf-8
import  time
import asyncio

async def run(x):
    print('waiting:%d'  % x)
start = time.time()
corountine = run(2)
loop = asyncio.get_event_loop()
# 将协程对象加入到事件循环，协程对象不能直接运行，在注册事件循环的时候，
#其实是run_until_complete方法将协程对象包装成了一个任务对象。
#task对象是Futurel类的子类，保存了协程运行后的状态，用于未来获取协程的结果
# 创建任务
task = asyncio.ensure_future(corountine)
print(task)
# #l另一种创建
# task = loop.create_task(corountine)
# 将协程对象加入到事件循环
loop.run_until_complete(task)
print(task)
end = time.time()
print("time",end-start)


#创建多个
loop =asyncio.get_event_loop()
tasks=[task1,task2]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
