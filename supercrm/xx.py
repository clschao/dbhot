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

