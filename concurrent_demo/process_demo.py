import os
import time
from multiprocessing import Process, Pool, cpu_count


#compute time
def metric(func):
    def wrapper(*args, **kwargs):
        print('{} start....'.format(func.__name__))
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('{} end:{}'.format(func.__name__, end - start))
        return r

    return wrapper


def my_task(num):
    print('son:[{}]{} {}'.format(num, os.getpid(),os.getppid()))
    time.sleep(1)
    print('---------end---------------')


#4s
@metric
def f1():
    for i in range(4):
        my_task(i)

#1s
@metric
def f2():
    processArr = []
    for i in range(4):
        p = Process(target=my_task, args=(i,))
        p.start()
        processArr.append(p)

    for p in processArr:
        p.join()

#pool
@metric
def f3():
    print(cpu_count())
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(my_task,args=(i,))

    pool.close()
    pool.join()



if __name__ == '__main__':
    f3()
