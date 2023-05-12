import urllib.request

url="http://www.ymmfa.com/read-gktid-1749887.html"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('gbk')

print(data)