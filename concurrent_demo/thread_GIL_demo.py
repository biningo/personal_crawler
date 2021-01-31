import threading
import time

from concurrent_demo.process_demo import metric

#more CPU task
def my_task():
    i = 0
    for _ in range(10000000):
        i = i + 1

@metric
def f1():
    for t in range(2):
        t = threading.Thread(target=my_task)
        t.start()
        t.join()

@metric
def f2():
    arr = []
    for t in range(2):
        t = threading.Thread(target=my_task)
        t.start()
        arr.append(t)

    for t in arr:
        t.join()


#more IO task
def my_sleep():
    time.sleep(1)

@metric
def f3():
    for t in range(4):
        t = threading.Thread(target=my_sleep)
        t.start()
        t.join()

@metric
def f4():
    arr = []
    for t in range(4):
        t = threading.Thread(target=my_sleep)
        t.start()
        arr.append(t)
    for t in arr:
        t.join()


#案例
count=0
def add_cpu(max_num):
    global count
    for i in range(max_num):
        count+=1

def f5(max_num):
    arr = []
    for t in range(10):
        t = threading.Thread(target=add_cpu,args=(max_num,))
        t.start()
        arr.append(t)
    for t in arr:
        t.join()



if __name__ == '__main__':
    # f1()
    # f2()
    # f3()
    # f4()
    count=0
    f5(10000)
    print(count)

    count=0
    f5(100000)
    print(count)