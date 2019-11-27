# coding= utf-8
from multiprocessing import Process


class SunProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("1234")

if __name__ == '__main__':
    p = SunProcess("sun")
    p.start()
    p.join()