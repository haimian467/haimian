import requests

cookies = {
    'fc0ee_readlog': '%2C1746492%2C18152%2C115639%2C1748014%2C1699182%2C1747980%2C1747917%2C1747974%2C1742232%2C142599%2C',
    'fc0ee_threadlog': '%2C18%2C52%2C46%2C39%2C21%2C19%2C32%2C36%2C11%2C45%2C',
    'fc0ee_ipstate': '1672446071',
    'fc0ee_ck_info': '%2F%09.ymmfa.com',
    'fc0ee_winduser': 'CVUDAAkBbFlQVwEBBQkOX1RSCQAHBQcLXVlTAlUDUAcBVgIGVlQDPA%3D%3D',
    'fc0ee_ol_offset': '9118',
    'fc0ee_lastpos': 'other',
    'fc0ee_lastvisit': '231%091672446486%09%2Fbbs%2Fdata%2Fq1.php%3F',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'fc0ee_readlog=%2C1746492%2C18152%2C115639%2C1748014%2C1699182%2C1747980%2C1747917%2C1747974%2C1742232%2C142599%2C; fc0ee_threadlog=%2C18%2C52%2C46%2C39%2C21%2C19%2C32%2C36%2C11%2C45%2C; fc0ee_ipstate=1672446071; fc0ee_ck_info=%2F%09.ymmfa.com; fc0ee_winduser=CVUDAAkBbFlQVwEBBQkOX1RSCQAHBQcLXVlTAlUDUAcBVgIGVlQDPA%3D%3D; fc0ee_ol_offset=9118; fc0ee_lastpos=other; fc0ee_lastvisit=231%091672446486%09%2Fbbs%2Fdata%2Fq1.php%3F',
    'Referer': 'http://www.ymmfa.com/read-gktid-142599.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
}

response = requests.get('http://www.ymmfa.com/bbs/data/q1.php', cookies=cookies, headers=headers, verify=False)
response.encoding = 'gbk'
print(response.text)
print(response)
