import gevent
from gevent import monkey;monkey.patch_all()
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor

def f2():
    print('f2')




if __name__ == '__main__':
    p = ProcessPoolExecutor()
    def f1():
        # p = Process(target=f2, )
        p.submit(f2,)
        # p.start()
        print('f1')

    g = gevent.spawn(f1)
    g.join()
    # gevent.joinall([g,])



# 添加了个新的业务处理函数
def test():
    print('哈哈哈')


def test2():
    print(22222)


def test3():
    print(33333)


def test4():
    print(44444)











