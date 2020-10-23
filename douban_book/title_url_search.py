import re
import execjs  # 这个库是PyExecJS
import requests
from douban_book.book_detail import book_info
# https://github.com/SergioJune/Spider-Crack-JS
# https://mp.weixin.qq.com/s/2mpu_oY2-M0wcLvf1eU7Sw
page_size=15
def book_url_crawler(text,limit=100):
    all_titles=[]
    all_urls = []
    current_page = 1
    count=0
    while count<limit:
        response = requests.get("https://search.douban.com/book/subject_search?search_text="+text+"&cat=1001&start="+str((current_page - 1) * page_size))
        r = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        # 导入js
        with open('main.js', 'r', encoding='gbk') as f:
            decrypt_js = f.read()
        ctx = execjs.compile(decrypt_js)
        data = ctx.call('decrypt', r)

        if len(data['payload']['items'])==1:
            all_titles += [item['title'] for item in data['payload']['items']]
            all_urls += [item['url'] for item in data['payload']['items']]
            return all_titles,all_urls
        all_titles += [item['title'] for item in data['payload']['items']]
        all_urls += [item['url'] for item in data['payload']['items']]

        current_count=len(data['payload']['items'])
        if current_count==0:
            break
        count+=current_count
        current_page+=1
    return all_titles,all_urls