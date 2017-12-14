#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))


from PublicModule.PublicCaseData import *
from PublicModule.CreateDataScript import *

class BCreateOrder(unittest.TestCase):
    u''''BA端单子'''

    def setUp(self):
        self.className = self.__class__.__name__


    def tearDown(self):
        pass

    def testBCreatOrder(self):
        scenarioLog(self.className, 'test' + self.className, u'开始准备下单')
        res = login(wgq_appkey,tel,password)#用户登陆
        self.assertEqual(res.get(u'message'),u'成功')#断言登陆成功
        scenarioLog(self.className,'test'+self.className,u'登陆成功')
        wgq_token = res.get(u'data').get(u'token')
        scenarioLog(self.className,'test'+self.className,u'开始创建下单地址')
        res = addAddress(wgq_token, wgq_appkey)  # 创建地址
        userAddressId = res.get("data").get("userAddressId")
        userId = res.get("data").get("userId")
        # print userAddressId,userId
        scenarioLog(self.className, 'test' + self.className, u'获取推荐时间')
        responseDict = getRecommendTime(wgq_token, wgq_appkey, userId)  # 获取推荐时间
        workdate = responseDict.get("data").get("workDate")
        worktime = responseDict.get("data").get("workTime")
        startTime = worktime.split("~")[0]
        endTime = worktime.split("~")[1]
        scenarioLog(self.className, 'test' + self.className, u'选择服务项目并下单')
        res = createThreePartOrder(wgq_token, wgq_appkey, workdate, startTime, endTime, userId, userAddressId)  # 创建b端订单。
        # print res
        self.assertEqual(res.get(u'message'),u'请求已成功处理')#断言下单成功
        workOrderNo = res.get(u'data').get(u'workOrderNo')
        scenarioLog(self.className, 'test' + self.className, workOrderNo)

        res = getOrderDetailInfo(wgq_token,wgq_appkey,workOrderNo)#订单详情
        # print res
        workOrderId = res.get(u'data').get(u'workOrderId')#获取workOrderId
        workOrderStatus = res.get(u'data').get(u'workOrderStatus')#获取订单状态
        Time = 40
        while Time:
            if workOrderStatus == 2:
                print u'已派工'
                break
            else:
                time.sleep(5)
                res = getOrderDetailInfo(wgq_token, wgq_appkey, workOrderNo)  # 订单详情
                workOrderStatus = res.get(u'data').get(u'workOrderStatus')  # 获取订单状态
                Time-=5
                if Time ==0:
                    print u'派工失败'

        #用户端处理订单
        orderOrderGoto(wgq_employeesC_token, wgq_employees_appkey, workOrderId)  # 师傅出发


        orderOrderService(wgq_employeesC_token, wgq_employees_appkey, workOrderId)  # 师傅上门


        orderSubmit(wgq_employeesC_token, wgq_employees_appkey, workOrderId)  # 提交订单

        orderSynOrderInfoForZJ(wgq_employeesC_token,wgq_employees_appkey,workOrderNo,workOrderId)#同步




    









