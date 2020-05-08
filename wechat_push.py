import json
import requests
response1 = requests.get(url="https://api.github.com/search/repositories?q=CVE-2020&sort=updated&order=desc")
response2 = requests.get(url="https://api.github.com/search/repositories?q=RCE&sort=updated&order=desc")

    #print(response1.text)
    #print(response2.text)
data1 = json.loads(response1.text)
data2 = json.loads(response2.text)
all_datas  = []
for i in data1['items']:
    s = [i['name'],i['html_url'],i['description']]
    if s not in all_datas:
        params = {
            "text":s[0],
            "desp":" 链接:"+str(s[1])+"\n简介"+str(s[2])
        }
        requests.get("https://sc.ftqq.com/SCU96954T628ed5500565032d8e20f10e914058925eb4be254fcde.send",params=params)
        print("推送完成")
        all_datas.append(s)