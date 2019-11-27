# coding= utf-8
# www.163.com www,baidu.com www.sohu.com www.google.com
#  3                           5                       2                            6
import  asyncio
import time
import threading

def start_loop(lp):
    # 启动事件循环
    asyncio.set_event_loop(lp)
    lp.run_forever()
async def wget(url):
    print("开始加载%s" % url)
    connect= asyncio.open_connection(url,80)
    print(connect)
    reader,writer = await connect
    # 连接成功
    header = "GET/HTTP\r\nHost:%s\r\n\r\n" %url
    writer.write(header.encode("utf-8"))
    await writer.drain()
    # 接收到数据
    while 1:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print("%s Header------%s"%(url,line.decode("urf-8").strip()))
    writer.close()

loop = asyncio.get_event_loop()
threading.Thread(target=start_loop,args=(loop,)).start()
# 给事件循环添加任务
for url in ["www.163.com", "www.baidu.com" ,
            "www.sohu.com" ]:
    asyncio.run_coroutine_threadsafe(wget(url),loop)