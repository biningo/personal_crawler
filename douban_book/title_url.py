from functools import reduce
import requests
from lxml import etree
from common_header import headers
type_map = {
        "评价": "S",
        "出版日期": "R",
        "综合": ""
}
page_size = 20
def book_title_url_crawler(tag,type,limit=1000):

    all_titles=[]
    all_urls=[]
    size=0

    current_page = 1
    url = "https://book.douban.com/tag/" + tag + "?start=" + str((current_page - 1) * page_size) + "&type=" + type
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)

    while len(selector.xpath("//span[@class='next']/a")) > 0:
        titles_e = selector.xpath("//div[@id='subject_list']//li//div[@class='info']/h2")
        for t in titles_e:
            all_titles.append(str(reduce(lambda x, y: x + y.strip(), t.xpath(".//text()"))).strip())
            all_urls.append(t.xpath(".//a/@href")[0])
            size+=1
            if size >= limit:
                return all_titles, all_urls
        current_page += 1
        url = "https://book.douban.com/tag/" + tag + "?start=" + str((current_page - 1) * page_size) + "&type=" + type
        resp = requests.get(url=url, headers=headers)
        selector = etree.HTML(resp.text)
    # 最后一页
    titles_e = selector.xpath("//div[@id='subject_list']//li//div[@class='info']/h2")
    for t in titles_e:
        all_titles.append(str(reduce(lambda x, y: x + y.strip(), t.xpath(".//text()"))).strip())
        all_urls.append(t.xpath(".//a/@href")[0])
        size+=1
        if size>=limit:
            return all_titles,all_urls
    return {k:v for k,v in zip(all_titles,all_urls)}