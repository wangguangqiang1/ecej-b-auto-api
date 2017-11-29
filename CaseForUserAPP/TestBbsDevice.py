#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *


class TestBbsDevice(unittest.TestCase):  #测试“在线的设备接口”接口

    def setUp(self):
        res = login(wgq_appkey, tel, password)  # 用户登陆
        wgq_token = res.get(u'data').get(u'token')
        self.url = url_Device#在线设备接口
        self.localData = {}
        self.localData['appKey'] = wgq_appkey
        self.localData['bussinessId'] = 361#商家ID
        self.localData['cityId'] = 2222 #城市id
        self.localData['token'] = wgq_token

    def tearDown(self):
        pass

    def test_001_normal_BbsDevice(self):
        res = requests.post(self.url,self.localData).json()
        # print res
        self.assertEqual(res.get(u'code'),200)
        self.assertEqual(res.get(u'message'),u'成功')
    def test_002_cityId_empty(self):
        self.localData['cityId'] = ''
        res = requests.post(self.url,self.localData).json()
        self.assertEqual(res.get(u'code'),220)
        self.assertEqual(res.get(u'message'),u'城市ID不能为空')