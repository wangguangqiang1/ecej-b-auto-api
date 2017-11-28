#! /user/bin/evn python
# coding:utf-8
'''
@author: 'luoyun'
@file: asda.py
@time: 2017/11/14 14:50
'''
from PublicModule.PublicClass import *
from PublicModule.CreateDataScript import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://siplatform.ecej.com:8989/base/index.html',
    'Cookie': 'UM_distinctid=15f703dcd7a60-0f90c17bdfcc838-4c322f7c-144000-15f703dcd7bf7; SESSION=f306bbf2-68bf-4045-abf4-6f0bbe1366a4',
    'Connection': 'keep-alive'
}

url = 'http://siplatform.ecej.com:8989/base/toLogin'

localData ={"loginName":"admin","password":"123456"}
# localData = None

res = requests.post(url,json = localData ,headers = headers)
print res
