import base64

from douban_book.title_url_search import book_url_crawler
from douban_book.book_detail import book_info_crawler
titles,urls = book_url_crawler('9780672338038',30,'douban_book/main.js')
print(len(titles))
print(titles)
print(urls)


for url in urls:
    info = book_info_crawler(url)
    for k,v in info.items():
        print(k,v)