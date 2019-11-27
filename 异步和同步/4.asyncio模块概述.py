# coding= utf-8
''''
python 3.4版本引入的标准库，直接内置了对异步io的支持
编程模式：是一个死循环，我们从async模块中直接获取一个EventLoop的引用，
然后把需要执行的协程扔到EventLoop中执行。就实现了异步

说明：到目前为止实现协程的不仅有async，还有gevent/tornado实现了类似的功能
关键字的说明：
1.event_loop 事件循环 开启无线循环，吧一些函数注册到事件循环中，当满足条件发生
                       时，我们会调用相应的协程函数
2.coroutine   协程对象，指一个使用async关键字定义的函数（如异步代码的函数），
                   他的调用不会立即执行函数，而是会返回一个协程对象，协程对象需要注册到
                   时间循环中，由事件循环调用
3.task任务    一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步的封装
4.future   代表将来要执行或没有执行的任务的结果，他和task没有本质的区别
5.async/await   用于定义3.5协程的关键字以前3.4用请注意，
async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
把@asyncio.coroutine替换为async；把yield from替换为await。
async定义一个协程，await用于阻塞异步调用接口

'''
import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(None)