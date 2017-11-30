#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *


class TestRecommentGetRecommendTime(unittest.TestCase):  #测试“用户评价”接口

    def setUp(self):
        res = login(wgq_appkey, tel, password)  # 用户登陆
        wgq_token = res.get(u'data').get(u'token')
        self.url = url_GetRecommendTime
        self.localData = {'token':wgq_token,'appKey':wgq_appkey}
        self.localData['bigClassId'] = 997
        self.localData['cityId'] = 2222
        self.localData['communityName'] = '关帝庙'
        self.localData['latitude'] = 33.635605
        self.localData['serviceClassId'] = 1184
        self.localData['uid'] = 'F982FAE7-9B50-4086-9531-51E6F1351AEB'
        self.localData['longitude'] = 114.650772
        self.localData['userId'] = 2479926

    def tearDown(self):
        pass

    def test_001_normal_TestRecommentGetRecommendTime(self):
        res = requests.post(self.url, self.localData).json()
        self.assertEqual(res.get(u'code'),200)
        self.assertEqual(res.get(u'message'),u'成功')