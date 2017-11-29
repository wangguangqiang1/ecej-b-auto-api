#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *


class TestBussinessCityListBybussinessInfo(unittest.TestCase):  #测试“根据商户ID获取商户服务的城市”接口

    def setUp(self):
        res = login(wgq_appkey, tel, password)  # 用户登陆
        wgq_token = res.get(u'data').get(u'token')
        self.url = url_CityListBybussinessInfo#获取商户服务的城市url
        self.localData = {}
        self.localData['appKey'] = wgq_appkey
        self.localData['bussinessId'] = 361#商户ID
        self.localData['token'] =wgq_token
    def tearDown(self):
        pass

    def test_001_normal_TestBussinessCityListBybussinessInfo(self):#正常传参
        res = requests.post(self.url,self.localData).json()
        # print res
        self.assertEqual(res.get(u'message'),u'成功')
        self.assertEqual(res.get(u'code'),200)
    def test_002_bussinessId_empty(self):
        self.localData['bussinessId'] = ''
        res = requests.post(self.url,self.localData).json()
        # print res
        self.assertEqual(res.get(u'code'),224)
        self.assertEqual(res.get(u'message'),u'商家ID不能为空')