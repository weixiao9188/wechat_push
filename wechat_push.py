# Title: wechat push CVE-2020
# Date: 2020-5-9
# Exploit Author: weixiao9188
# Version: 3.0
# Tested on: Linux,windows
# coding:UTF-8
import requests
import json
import time
import os
import pandas as pd
time_sleep = 20 #每隔20秒爬取一次
while(True):
    #判断文件是否存在
    datas = []
    if os.path.exists("olddata.csv"):
        datas = pd.read_csv("olddata.csv", header=None).values.tolist()
    else:
        datas = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
    response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&order=desc",headers=headers)
    response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&sort=updated&order=desc",headers=headers)
    data1 = json.loads(response1.text)
    data2 = json.loads(response2.text)
    for j in [data1["items"],data2["items"]]:
        for i in j:
            s = {"name":i['name'],"html":i['html_url'],"description":i['description']}
            s1 = [i['name'],i['html_url'],i['description']]
            if s1 not in datas:
                params = {
                     "text":s["name"],
                    "desp":" 链接:"+str(s["html"])+"\n简介"+str(s["description"])
                }
                print("当前推送为"+str(s))
                requests.get("https://sc.ftqq.com/xxxx.send",params=params)
                time.sleep(1)#以防推送太猛
                print("推送完成")
                datas.append(s1)
            else:
                print("数据已处在")
    pd.DataFrame(datas).to_csv("olddata.csv",header=None,index=None)
    time.sleep(time_sleep)
