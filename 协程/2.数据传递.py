# coding= utf-8


def func():
    data ="#"
    #yield不但可以返回一个值，并且他还可以接收调用者发送的参数
    r = yield data
    print("----------------1",r,data)
    r = yield data
    print("----------------2",r,data)
    r = yield data
    print("----------------3",r,data)
    r = yield data

g = func()
print(g, type(g))
# next(g)
# next(g)
# next(g)
# next(g)
#启动g
print(g.send(None))
# 传参数，yield接收，即r=a
print(g.send("a"))