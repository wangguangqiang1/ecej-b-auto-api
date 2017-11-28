#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

from PublicModule.PublicClass import *


filePath =  os.path.abspath('%s../../TestReport' % sys.path[0]+'/'+'RunAllCase-'+ time.strftime('%Y-%m',time.localtime(time.time())))
sentEmail(filePath,u'ECEJ-测试报告')

