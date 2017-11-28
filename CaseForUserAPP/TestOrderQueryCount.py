#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os



from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *


class TestOrderQueryCount(unittest.TestCase):  #测试我的接口

    def setUp(self):
        res = login(wgq_appkey, tel, password)  # 用户登陆
        wgq_token = res.get(u'data').get(u'token')
        self.url = url_Count#我的接口
        self.localData = {'token':wgq_token,'appKey':wgq_appkey}
        self.localData['orderSourceListStr'] = '15,16'
        self.localData['serviceType'] = 'dayOrderNumber'
        self.localData['threepartyMerchanId'] = 2

    def tearDown(self):
        pass

    def test_001_normal_TestOrderQueryCount(self):
        res = postRequest(self.url,self.localData)
        print res
        self.assertEqual(res.get(u'message'),u'请求已成功处理')
        self.assertEqual(res.get(u'code'),200)
