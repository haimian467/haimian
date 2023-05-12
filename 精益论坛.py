#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/14 19:21
# @Author  : 什么都不会的小博
# @File    : 精益论坛.py
import requests
import random
import re
import time
from lxml import etree


def dailyTask():
    headers = {
        'cookie': 'HMACCOUNT_BFESS=8C37D819A1BB855B; ZFY=mpGDJE1A:BZfzoQuvNeX9ekSMZRb35v9ZOB1YIhJ4hBs:C; BAIDUID_BFESS=DBFCB1EE2EAC50F510439A961E34E3CC:FG=1; BDUSS_BFESS=JGUDY4a2MzN1F1MkUxdHVUQTdKbFlBUmZWYVFWdkRrblNzYmdvM2NxaE12d0ZrRVFBQUFBJCQAAAAAAAAAAAEAAAActYSj2sDfz0Q2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEwy2mNMMtpjbl',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
    }
    # for i in range(5):
    session = requests.session()
    pageNumber = random.randint(0, 5)
    url_page = 'https://bbs.125.la/plugin.php?id=dsu_paulsign:sign'
    rep = session.get(url=url_page, headers=headers)
    temp = re.findall(r'/thread-14(.*).html" target="_blank"', rep.text)
    formhash = re.findall(r'formhash=(.*)">退出', rep.text)
    # print(formhash)
    url_page = 'https://bbs.125.la/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1'
    rep = session.post(url=url_page, headers=headers,
                       data={'formhash': formhash, "submit": "1", "targerurl": "", "todaysay": "", "qdxq": "kx"})
    print(rep.text)
    for i in range(0, len(temp)):
        url_page = 'https://bbs.125.la/thread-14' + temp[i] + '.html'
        rep = session.get(url=url_page, headers=headers)
        if rep.status_code == 200:
            # print('进入帖子详情页成功')
            tree = etree.HTML(rep.text)
            a_list = tree.xpath('//*[@id="ak_rate"]/@onclick')
            addr = a_list[0]
            str1 = addr.split(',')
            str2 = str1[1].split('&')
            tid1 = str2[2]
            pid1 = str2[3]
            tid2 = tid1.split('=')[1]
            pid2 = pid1.split('=')[1]
            pid3 = pid2.split('\'')[0]
            tid = tid2
            pid = pid3  # 获取到tid与pid
            formash1 = tree.xpath('//*[@id="vfastpost"]/input/@value')
            formash = formash1[0]  # 获取到formash
            # print("获取pid={}与tid={}与formash={}成功，开始自动评分".format(pid, tid, formash))
            # 开始评分
            url_score = 'https://bbs.125.la/forum.php?mod=misc&action=rate&ratesubmit=yes&infloat=yes&inajax=1'
            data = 'formhash=' + formash + '&tid=' + tid + '&pid=' + pid + '&referer=https%3A%2F%2Fbbs.125.la%2Fforum.php%3Fmod%3Dviewthread%26tid%3D' + tid + '%26page%3D0%23pid' + pid + '&handlekey=rate&score4=%2B1&reason=%E6%84%9F%E8%B0%A2%E5%88%86%E4%BA%AB%EF%BC%8C%E5%BE%88%E7%BB%99%E5%8A%9B%EF%BC%81%7E'
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            headers['Referer'] = 'https://bbs.125.la/thread-14720892-1-1.html'
            rep_score = session.post(url=url_score, data=data, headers=headers)
            # print(1)
            # print(rep_score.status_code)
            # print(rep_score.text)
            print("评分结果:" + re.findall(r'CDATA\[(.*)<scrip', rep_score.text)[0])
            time.sleep(1)
            x = rep_score.text.find("超过限制")
            if x != -1:
                break;


        else:
            print('进入帖子失败')


if __name__ == '__main__':
    dailyTask()