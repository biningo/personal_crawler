import requests
from common_header import headers
from lxml import etree


def book_directory(url: str):
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)
    id = "dir_" + url.split('/')[-2] + "_full"
    return '\n'.join(list(map(lambda x: x.strip().replace('\u3000', '').replace('\t', ''),
                              selector.xpath("//div[@id='" + id + "']//text()")))[:-3])


# 清理工具函数
def clear_text(content):
    return list(filter(lambda x: x != '', list(map(lambda x: x.strip(), content))))


def book_info(url: str):
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)
    book_name = ''.join(clear_text(selector.xpath("//div[@id='wrapper']/h1//text()")))
    # book_name = ''.join(selector.xpath("//div[@id='wrapper']/h1//text()]")).strip()
    titles = clear_text(selector.xpath("//div[@id='info']/span[@class='pl']/text()"))
    values = list(
        filter(lambda x: x != ':', clear_text(selector.xpath("//div[@id='info']/text() | //div[@id='info']/a/text()"))))
    titles = list(map(lambda x: x.replace(':', ''), titles))
    aSpan = selector.xpath("//div[@id='info']/span[not(@class)]")
    for v in aSpan:
        titles2 = v.xpath(".//span[@class='pl']//text()")
        values2 = v.xpath(".//a//text()")
        title = ''.join(titles2).strip()
        value = '/'.join(values2).strip()

        titles.append(title)
        values.append(value)
    info = {}
    info['书名'] = book_name
    for k, v in zip(titles, values):
        info[k] = v
    info['评分'] = ''.join(selector.xpath("//div[@id='interest_sectl']//strong/text()")).strip()
    info['目录'] = book_directory(url)
    return info