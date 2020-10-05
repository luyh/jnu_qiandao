#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os
from send_email import  send_email



def login():
        username = os.environ.get('USERNAME')
        password = os.environ.get('PASSWORD')

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

        #send_email(title='jnu 体温签到', content=response.text)

def qiandao():
        url = 'https://stuhealth.jnu.edu.cn/api/write/main'
        personNo = os.environ.get('personNo')
        personName = os.environ.get('personName')
        phone = os.environ.get('phone')
        assistantName = os.environ.get('assistantName')
        linkman = os.environ.get('linkman')
        linkmanPhone = os.environ.get('linkmanPhone')
        jnuid = os.environ.get('jnuid')

        body = {"mainTable":{"wayStart":"2020-01-10","arriveTime":"2020-01-12","way2Start":"","language":"cn","declareTime":"2020-04-17","personNo":personNo,"personName":personName,"sex":"男","professionName":"信号与信息处理[081002]","collegeName":"信息科学技术学院","phoneArea":"+86","phone":phone,"assistantName":assistantName,"assistantNo":"0006131*","className":"12级计算机班","linkman":linkman,"linkmanPhoneArea":"+86","linkmanPhone":linkmanPhone,"personHealth":"1","temperature":"36.5","personHealth2":"0","leaveState":"1","leaveHubei":"0","wayType1":"0","wayType2":"1","wayType3":"0","wayType5":"0","wayType6":"0","wayNo":"火车","currentArea":"2","inChina":"1","personC1id":"330000","personC1":"浙江省","personC2id":"330100","personC2":"杭州市","personC3id":"330110","personC3":"余杭区","personC4":"东海水景城","otherC4":"无","isPass14C1":"0","isPass14C2":"0","isPass14C3":"0"},"jnuid":jnuid}

        headers = {
        'accept':'application/json,text/plain,*/*',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'zh-CN,zh;q=0.9',
        'content-length':'959',
        'content-type':'application/json',
        'Origin': 'https://stuhealth.jnu.edu.cn',
        'referer':'https://stuhealth.jnu.edu.cn/',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

        }

        print (json.dumps(body))
        # print type(json.dumps(body))
        # 这里有个细节，如果body需要json形式的话，需要做处理
        # 可以是data = json.dumps(body)
        response = requests.post(url, data=json.dumps(body), headers=headers)
        #response = requests.post(url, data=body, headers=headers)
        # 也可以直接将data字段换成json字段，2.4.3版本之后支持
        # response  = requests.post(url, json = body, headers = headers)

        # 返回信息
        print(response.text)
        # 返回响应头
        print(response.status_code)

        #send_email(title='jnu 体温签到', content=response.text)

qiandao()

print('while loop forever')

while True:
        pass
