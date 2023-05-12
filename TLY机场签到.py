# -*- coding: utf-8 -*-
# @Time    : 2023-03-02 16:34
# @Author  : 什么也不会的小博
# @Site    : 
# @File    : tly机场签到2.0.py
# @Software: PyCharm 
# @Comment :
import time
import requests
import base64
import json
from datetime import datetime

cookie = "cf_clearance=VGvbbOOenmCCNtoQNWDl0FWqNZhPxS2SpwRKPESiNsc-1680658268-0-150; is_web=1; lang=zh; _ga=GA1.2.1565749279.1680658279; _gid=GA1.2.943945454.1680658279; __cf_bm=LHgstXCa.5Z2ykrR2eF7FpmdYx3xPCjc1z4sT64THW4-1680658280-0-AQMu8lYzbQdE5fiJDYOLUfgd4V/twIk2IfBhWBn5oONLQhMoXolv0J4RHbfCnproaD0EsUoJnFIhL4s3M5OT9r6RT+GJhUhetem190kkYy3ECP/uaqczNMuL1YiLj4mccA==; PHPSESSID=5s5mn6ljj0n6h20dhr1p7uvtn0; user_pwd=86e7e55f4fde28625ac36db156bd84de1715873b0d34e; uid=2289903; user_email=1515497426%40qq.com"
token = '370aa7ba4'  # 验证码token


# token在http://www.bhshare.cn/imgcode/gettoken/ 自行申请

def imgcode_online(imgurl):
    data = {

        'token': token,
        'type': 'online',
        'uri': imgurl
    }
    response = requests.post('http://www.bhshare.cn/imgcode/', data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200:
        print(result['data'])
        return result['data']
    else:
        print(result['msg'])
        return 'error'


def getmidstring(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


def tly():
    signUrl = "https://tly22.com/modules/index.php"
    hearder = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Cookie': cookie}

    res = requests.get(url=signUrl, headers=hearder).text
    signtime = getmidstring(res, '<p>上次签到时间：<code>', '</code></p>')
    timeArray = time.strptime(signtime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    t = int(time.time())

    if t - timeStamp > 86400:
        print("距上次签到时间大于24小时啦,可签到")
        done = False
        while (done == False):
            # 获取验证码图片
            captchaUrl = "https://tly22.com/other/captcha.php"
            signurl = "https://tly22.com/modules/_checkin.php?captcha="
            hearder = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
                'Cookie': cookie}
            res1 = requests.get(url=captchaUrl, headers=hearder)
            base64_data = base64.b64encode(res1.content)
            oocr = imgcode_online('data:image/jpeg;base64,' + str(base64_data, 'utf-8'))
            res2 = requests.get(url=signurl + oocr.upper(), headers=hearder).text
            print(res2)
            findresult = res2.find("流量")
            if findresult != -1:
                done = True
            else:
                done = False
                print("未签到成功，沉睡3秒再来一次")
                time.sleep(3)

    else:
        print("还未到时间！", t - timeStamp)


def main_handler(event, context):
    tly()


if __name__ == '__main__':
    tly()
