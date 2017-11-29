#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'
import os
import sys
import time

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

from CaseForScenario.BCreateOrder import *
from CaseForUserAPP.TestLoginLoginIndex import TestLoginLoginIndex
from CaseForUserAPP.TestAddAddress1 import TestAddAddress1
from CaseForUserAPP.TestOrderQueryCount import TestOrderQueryCount
from CaseForUserAPP.TestBussinessCityListBybussinessInfo import TestBussinessCityListBybussinessInfo
from CaseForUserAPP.TestBbsDevice import TestBbsDevice



def output():
    suite = unittest.TestSuite()
    suite.addTest(BCreateOrder('testBCreatOrder'))
    suite.addTest(TestLoginLoginIndex('test_001_normal_TestLoginLoginIndex'))
    suite.addTest(TestAddAddress1('test_TestAddAddress_001_nomnal'))
    suite.addTest(TestOrderQueryCount('test_001_normal_TestOrderQueryCount'))
    suite.addTest(TestBussinessCityListBybussinessInfo('test_001_normal_TestBussinessCityListBybussinessInfo'))
    suite.addTest(TestBbsDevice('test_001_normal_BbsDevice'))

    fileSearch = 'RunAllCase-' + time.strftime('%Y-%m', time.localtime(time.time()))  # 测试报告文件夹名称
    # fileSearch = 'RunAllCase-'+ '2017-04'
    # print fileSearch
    fileSuffix = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))  # 测试报告文件时间后缀
    # print fileSuffix
    filePath = os.path.abspath(
        '%s../../TestReport' % sys.path[
            0] + '/' + fileSearch + '/RunAllCaseResult_' + fileSuffix + '.html')  # 测试报告文件的完整路径

    try:
        fp = file(filePath, 'w') #定义测试报告的标题和内容参数，并存储到相应位置
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'ECEJ全部接口测试报告',
                                               description=u'测试用例执行结果： ') #使用HTMLTestRunner的框架输出报告
        result = runner.run(suite)
        # print type(result)
        logfile = open(r'runLog.txt', 'a')
        logfile.write('\n%s' % str(result) + time.strftime(' %Y-%m-%d %H:%M:%S', time.localtime(time.time()))) #运行记录写日志
        logfile.close()

        if (result.failure_count or result.error_count):#控制台输出，只要遇到错误和断言失败，均认为本次测试总结果是失败的
            print 'Not pass'
        else:
            print 'pass' #全部通过视为通过
    except IOError, e:
        print e
        os.makedirs(os.path.abspath('%s../../TestReport' % sys.path[0] + '/' + fileSearch)) #发现存储目标文件夹不存在，则创建
        output()


output()
