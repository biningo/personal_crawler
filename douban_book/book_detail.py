import requests
from common_header import headers
from lxml import etree
def book_directory(url: str):
    resp = requests.get(url=url, headers=headers)
    selector = etree.HTML(resp.text)
    id = "dir_" + url.split('/')[-2] + "_full"
    return '\n'.join(list(map(lambda x: x.strip().replace('\u3000','').replace('\t',''), selector.xpath("//div[@id='" + id + "']//text()")))[:-3])