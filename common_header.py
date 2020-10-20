from datetime import datetime
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
    "Date":datetime.utcnow().strftime(GMT_FORMAT),
}

# //最好删除这个请求头防止乱码
# "Accept-Encoding": "gzip, deflate, br"

