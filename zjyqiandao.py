#职教云自动签到
#二改作者：小博
import requests
import json
import datetime
print("作者已开源。支持开源共享精神，共创美好明天。新版职教云签到，切勿非法用途!!!")
print("三秒后开始执行脚本")
print("3")
print("2")
print("1")
#全局变量区
user="201940621056"
passwd='Zhengyanbo123@'
#================================
#这个登录方式是用作exe软件
#user = input("账号：")  # 账号
#passwd = input("密码：")  # 密码
#==================================
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; 2206122SC Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 whatyApp whatyApiApp","content-type": "multipart/form-data; boundary=---011000010111000001101001"}
Authorization='Bearer '#职教权鉴
classsign=[]
#全局结束
def login():  #登录职教云获取token并获取权鉴
    global Authorization,headers
    payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n"+user+"\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"passwd\"\r\n\r\n"+passwd+"\r\n-----011000010111000001101001--\r\n\r\n"
    querystring = {"token": json.loads(requests.request("POST", "https://user.icve.com.cn/m/peMobileLogin_accountLogin.action", data=payload, headers=headers).text)['token']}
    Authorization = Authorization+json.loads(requests.request("POST", "https://user.icve.com.cn/m/zhzjMobile_getRestSsoToken.action", params=querystring).text)['data']["userAccessToken"]
    headers["Authorization"]=Authorization
def getclass():#获取当日课程及其进行中的签到
    global headers
    classid=[]
    del headers["content-type"]
    headers['Host']='spoc-classroom.icve.com.cn'
    payload = {"params": {"startDate": datetime.datetime.now().strftime("%Y-%m-%d"),"current": 1,"size": 8}}
    for i in json.loads(requests.request("POST", "https://user.icve.com.cn/classroom-teaching-api/classroom/getClassroomByStudent", json=payload, headers=headers).text)['data']['data']["records"]:
        classid.append([i['id'],i["courseName"]])
    for i in classid:
        payload = {"params": {"classroomId": i[0],"classroomTypeCode": 1},"page": {"curPage": 1,"pageSize": 10,"totalCount": 0,"totalPage": 0}}
        for o in json.loads(requests.request("POST", "https://spoc-classroom.icve.com.cn/classroom-teaching-api/peClassroomActivity/student/classroomActivityList", json=payload, headers=headers).text)['data']["items"]:
            if o["typeName"]=="签到":
                if '已签到' not in requests.request("POST","https://spoc-classroom.icve.com.cn/classroom-teaching-api/sign/student/getSignResult",json={"params": {"id": o["recordId"]}}, headers=headers).text:
                    classsign.append([o["recordId"],o["id"],o["classroomName"],i[1]])
    del headers["Host"]
def gosign():#启动签到
    if "0" not in str(len(classsign)):
        for i in classsign:
            r=requests.request("POST","https://spoc-classroom.icve.com.cn/classroom-teaching-api/sign/student/updateSignStatus",
                                json={"params": {"id": i[0],
                                                 "activityId": i[1]}}, headers=headers)
            if '签到成功' in r.text:
                print(i[3]+i[2]+'签到成功')
    else:
        print("执行完毕没有可签到的项目")

if __name__ == '__main__':
    login()
    getclass()
    gosign()