#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os


from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import postRequest


class TestLoginLoginIndex(unittest.TestCase):  #测试“登陆接口”接口

    def setUp(self):
        self.url = url_LoginIndex#接口地址
        self.localData={}
        self.localData['appKey'] = wgq_appkey
        self.localData['tel'] = 18518980784
        self.localData['password'] = '25F9E794323B453885F5181F1B624D0B'

    def tearDown(self):
        pass

    def test_001_normal_TestLoginLoginIndex(self):#全部正确参数的case，用户回归拨测
        res = postRequest(self.url,self.localData)#发送请求
        # print res
        self.assertEqual(res.get(u'message'),u'成功')
        self.assertEqual(res.get(u'code'),200)
        self.assertEqual(res.get(u'data').get(u'loginName'),u'18518980784')
        self.assertEqual(res.get(u'data').get(u'tel'),u'18518980784')
        self.assertEqual(res.get(u'data').get(u'businessId'),361)
        self.assertEqual(res.get(u'data').get(u'bussinessName'),u'王广强商家')
        self.assertEqual(res.get(u'data').get(u'address'),u'周口市川汇区')

    def test_002_appKey_empty(self):#传空
        self.localData['appKey'] = ''
        res = postRequest(self.url,self.localData)#发送请求
        # print json.dumps(res).decode('unicode-escape')  # 返回数据unicode解码查看
        self.assertEqual(res.get(u'message'),u'非法连接')
        self.assertEqual(res.get(u'code'),505)

    def test_003_appKey_lack(self):#不传
        self.localData.pop('appKey')
        res = postRequest(self.url,self.localData)
        # print json.dumps(res).decode('unicode-escape')  # 返回数据unicode解码查看
        self.assertEqual(res.get(u'message'),u'非法连接')
        self.assertEqual(res.get(u'code'),505)

    def test_004_appKey_wrong(self):#传错
        self.localData['appKey'] = -5
        res = postRequest(self.url,self.localData)
        # print json.dumps(res).decode('unicode-escape')  # 返回数据unicode解码查看
        self.assertEqual(res.get(u'message'),u'非法连接')
        self.assertEqual(res.get(u'code'),505)

    def test_005_appKey_type(self):#传错类型
        self.localData['appKey'] = True
        res = postRequest(self.url,self.localData)
        self.assertEqual(res.get(u'message'),u'非法连接')
        self.assertEqual(res.get(u'code'),505)

    def test_006_tel_empty(self):  # 传空
        self.localData['tel'] = ''
        res = postRequest(self.url, self.localData)  # 发送请求
        # print json.dumps(res).decode('unicode-escape')  # 返回数据unicode解码查看
        self.assertEqual(res.get(u'message'), u'账号不能为空')
        self.assertEqual(res.get(u'code'), 230)

    def test_007_tel_lack(self):  # 不传
        self.localData.pop('tel')
        res = requests.post(self.url, self.localData)
        # print res
        self.assertEqual(res.status_code,404)

    def test_008_appKey_wrong(self):  # 传错
        self.localData['tel'] = -5
        res = postRequest(self.url, self.localData)
        # print json.dumps(res).decode('unicode-escape')  # 返回数据unicode解码查看
        self.assertEqual(res.get(u'message'), u'账号不存在')
        self.assertEqual(res.get(u'code'), 227)

    def test_009_tel_type(self):  # 传错类型
        self.localData['tel'] = True
        res = postRequest(self.url, self.localData)
        # print json.dumps(res).decode('unicode-escape')
        self.assertEqual(res.get(u'message'), u'账号不存在')
        self.assertEqual(res.get(u'code'), 227)

