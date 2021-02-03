import multiprocessing
import threading

import requests

from concurrent_demo.process_demo import metric

page_size = 10
path = '/home/pb/tmp/image'


def get_url(page):
    url = 'https://500px.com.cn/discover/rating?resourceType=0,2' + \
          '&category=&orderBy=rating&photographerType=&startTime=&page={}&size={}&type=json'.format(page, page_size)
    resp = requests.get(url=url)
    body = resp.json()['data']
    for item in body:
        img_p3_url = item['url']['baseUrl'] + '!p3'
        print(img_p3_url)


@metric
def run1():
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for i in range(1, 11):
        pool.apply_async(get_url, args=(i,))
    pool.close()
    pool.join()


@metric
def run2():
    for i in range(1, 11):
        get_url(i)


@metric
def run3():
    arr = []
    for i in range(1, 11):
        t = threading.Thread(target=get_url, args=(i,))
        t.start()
        arr.append(t)
    for t in arr:
        t.join()


if __name__ == '__main__':
    run1()
    run3()
    run2()
