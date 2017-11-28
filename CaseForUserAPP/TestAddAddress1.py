#! /user/bin/evn python
# coding:utf-8
'''
@author: 'luoyun'
@file: TestAddAddress.py
@time: 2017/11/9 14:20
'''


from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import creat_AddAddress

class TestAddAddress1(unittest.TestCase):
    '''haha'''
    def setUp(self):
        self.localData = wjb_create_addAddress_localData.copy()

    def tearDown(self):
        pass

    def test_TestAddAddress_001_nomnal(self):
        localData = self.localData
        res = creat_AddAddress(localData)
        self.assertEqual(res.get(u'message'),u'成功')
        self.assertEqual(res.get(u'code'), 200)
