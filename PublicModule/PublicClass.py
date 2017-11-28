#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os
import types
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

import unittest
import requests
import json
import random
import struct
import time
import string
from RunClass import HTMLTestRunner

from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText

from PublicModule.PublicCaseData import *


# 邮件发送服务
def sentEmail(filePath, Subject):#将测试报告文件作为形参
    try:
        fileName = os.listdir(filePath)#取文件夹内最新的测试报告
        fileName.sort()
        fileName = fileName[-1]
        # print fileName#,type(fileName)
        # print filePath + '\\'+fileName #测试报告前增加路径

        soup = BeautifulSoup(open(filePath + '/' + fileName), "html.parser") #正则匹配 能按照标准的缩进格式的结构输出:
        print filePath + '/' + fileName
        logfile = open(os.path.abspath('%s../../RunLog' % sys.path[0] + '/result.html'), 'w')
        logfile.write('\n%s'% soup)
        logfile.close()
        logfile = open(os.path.abspath('%s../../RunLog' % sys.path[0] + '/result.html'))
        print os.path.abspath('%s../../RunLog' % sys.path[0] + '/result.html')
        testReport = logfile.read()
        for i in soup.table.select('.hiddenRow'):
            testReport = testReport.replace("%s" % i, '')
        for i in soup.table.select('.'):
            testReport = testReport.replace("%s" % i, '')
        for i in soup.find_all(name='a'):
            testReport = testReport.replace("%s" % i, '')
        # 邮件发送
        # testReport = open(filePath + '/'+fileName,'r').read() #读取报告
        # print type(testreport)
        msg = MIMEMultipart('alternative') #创建邮件内容集合
        msg["Subject"] = Subject #邮件主题
        msg["From"] = user #发布者
        content = MIMEText(testReport, 'html', 'utf-8') #邮件文字内容
        # content = MIMEText(u'sofk',_subtype='plain',_charset='gb2312') #邮件文字内容test_001_normal_CartGet
        # print content

        #创建附件
        att = MIMEText(open(filePath + '/' + fileName, 'rb').read(), 'base64', 'utf-8')
        # print att
        att["Content-Type"] = 'text/xml;CHARSET=GB2312'
        att["Content-Disposition"] = "attachment; filename=%s" % fileName #附件文件名称为测试报告文件名称

        #向邮件内容集合内添加正文和附件
        msg.attach(content)
        logfile.close()
        s = smtplib.SMTP_SSL(sentSevice) #邮件发送服务器
        s.login(user, pwd) #登录邮箱
        s.sendmail(user, to, msg.as_string()) #发送邮件，包含发送者，接收者，邮件内容
        s.quit() #关闭服务连接
        print "Success!" #输出发送结果
        logfile = open(os.path.abspath('%s../../RunLog' % sys.path[0] + '/EmailLog.txt'), 'a')
        logfile.write('\n发送成功' + time.strftime(' %Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        logfile.close()

    except Exception, e: #捕获错误码内容
        print "Falied,%s" % e
        logfile = open(os.path.abspath('%s../../RunLog' % sys.path[0] + '/EmailLog.txt'), 'a')
        logfile.write('\n发送失败,%s' % str(e) + time.strftime(' %Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        logfile.close()


