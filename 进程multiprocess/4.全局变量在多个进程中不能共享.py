# coding= utf-8
from multiprocessing import Process
from time import sleep

money = 0
def run():
    print("启动子进程1")
    global money
    print(money)
    sleep(1)
    print(money)
    money = 300
    print(money)
    print("结束子进程1")

def run2():
    print("启动子进程2")
    global money
    print(money)
    sleep(3)
    money = 20
    print(money)
    print("结束子进程2")

if __name__ == '__main__':
    print("启动主进程")
    # 创建子进程时会将主进程的资源拷贝到子进程中，
    # 子进程单独有1分主进程的数据，相互不影响
    p = Process(target=run)
    p1 = Process(target=run2)
    p.start()
    p1.start()
    p.join()
    p1.join()
    print(money)
    print("结束主进程")