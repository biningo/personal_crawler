import requests
from common_header import headers
from lxml import etree
def book_directory(url: str):
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)
    id = "dir_" + url.split('/')[-2] + "_full"
    return '\n'.join(list(map(lambda x: x.strip().replace('\u3000', '').replace('\t', ''),
                              selector.xpath("//div[@id='" + id + "']//text()")))[:-3])

#清理工具函数
def clear_text(content):
    return list(filter(lambda x: x != '', list(map(lambda x: x.strip(), content))))

def book_info(url: str):
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)
    titles = clear_text(selector.xpath("//div[@id='info']/span[@class='pl']/text()"))
    titles = list(map(lambda x:x.replace(':',''),titles))
    values = clear_text(selector.xpath("//div[@id='info']/text()"))
    info = {}
    for k,v in zip(titles, values):
        info[k] = v
    aSpan = selector.xpath("//div[@id='info']/span[not(@class)]")
    for v in aSpan:
        titles = v.xpath(".//span[@class='pl']//text()")
        values = v.xpath(".//a//text()")
        title = ''.join(titles).strip()
        value = '/'.join(values).strip()
        info[title] = value
    info['评分'] = ''.join(selector.xpath("//div[@id='interest_sectl']//strong/text()")).strip()
    info['目录'] = book_directory(url)
    return info