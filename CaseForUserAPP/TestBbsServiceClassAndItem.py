#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *


class TestBbsServiceClassAndItem(unittest.TestCase):  #测试“B端在线的品类项目接口”接口

    def setUp(self):
        res = login(wgq_appkey, tel, password)  # 用户登陆
        wgq_token = res.get(u'data').get(u'token')
        self.url = url_ServiceClassAndItem
        self.localData = {}
        self.localData['appKey'] = wgq_appkey
        self.localData['bussinessId'] = bussinessId
        self.localData['cityId'] = cityId
        self.localData['deviceId'] = deviceId
        self.localData['token'] = wgq_token

    def tearDown(self):
        pass

    def test_001_normal_TestBbsServiceClassAndItem(self):
        res = requests.post(self.url,self.localData).json()
        # print res
        self.assertEqual(res.get(u'code'),200)
        self.assertEqual(res.get(u'message'),u'成功')