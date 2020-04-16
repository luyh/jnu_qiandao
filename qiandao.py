#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os
from send_email import  send_email

username = os.environ.get( 'USERNAME' )
password = os.environ.get( 'PASSWORD' )

url = 'https://stuhealth.jnu.edu.cn/api/user/login'
body = {"username":username,"password":password}

headers = {
        'Host': 'stuhealth.jnu.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '63',
        'Accept': 'application/json,text/plain,*/*',
        'Origin': 'https://stuhealth.jnu.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Content-Type': 'application/json',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https//stuhealth.jnu.edu.cn/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
}

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, data=json.dumps(body), headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)

# 返回信息
print(response.text)
# 返回响应头
print(response.status_code)

send_email(title='jnu 体温签到', content=response.text)

print('while loop forever')

while True:
        pass