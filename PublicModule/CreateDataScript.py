#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os

sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

import random
import urllib
import urllib2
import cookielib
from PIL import Image
import re
import pytesseract
from json import loads


from PublicModule.PublicCaseData import *
from requests_toolbelt import MultipartEncoder

os.chdir(os.path.abspath('%s../../pytesser_v0.0.1' % sys.path[0]))

#商家app登陆
def login(appKey,tel,password):
    url = url_LoginIndex
    localData = {'appKey':appKey,'tel':tel,'password':password}
    res = requests.post(url,localData).json()
    return res

#requests.post 请求
def postRequest(urlStr, requestData):
    try:
        res = requests.post(urlStr, requestData).json()
    except Exception, e:
        print "Error:" + str(e.message)
        return 0
    return res

def chineseCharacters(num): #汉字
    s = ""
    while num:
        a = random.randint(0xbf, 0xd7)
        b = random.randint(0xa1, 0xfe)
        c = struct.pack("BB", a, b)
        try:
            s += c.decode("gb2312")
            num -= 1
        except UnicodeDecodeError:
            pass
    return s.encode("utf-8")

def rdmString(num):#字符串
    base = ''
    for i in range(num):
        data = random.choice(string.letters + string.digits)
        base = base + data
    return unicode(base)

def scenarioLog(className, defName, otherOne):#场景步骤日志
    print  '[%s]-[%s]-[%s]-[%s]' % (
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), className, defName, otherOne)

#创建订单地址 王广强
def addAddress(token,appKey):
    requestData = {'token':token,'appKey':appKey}
    requestData['cityId'] = '2222'
    requestData['cityName'] = '周口'
    requestData['detailAddress'] = chineseCharacters(2) #随机地址
    requestData['districtInfo'] = 'community:周口师范学院,longitude:114.689163,latitude:33.641472'
    requestData['phone'] = '18518980784'
    requestData['userName'] = '王广强'
    res = requests.post(url_AddAddress,requestData).json()
    return res


#获取推荐时间
def getRecommendTime(token,appKey,userId):
    requestData = {'token':token,'appKey':appKey}
    requestData['cityId'] = 2222
    requestData['communityName'] = "周口师范学院"
    requestData['latitude'] = "33.641472"
    requestData['longitude'] = "114.689163"
    requestData['serviceClassId'] = 1184
    requestData['bigClassId'] = 997
    requestData['uid'] = "127D1C8F-D782-4F9F-A361-DD2915BB1FE5"
    requestData['userId'] = userId
    res = requests.post(url_GetRecommendTime,requestData).json()
    return res

#b端创建订单
def createThreePartOrder(token,appKey,workDate,startTime,endTime,userId,userAddressId):
    values ={
              "operUser" : "18518980784",
              "userId" : userId,
              "guid" : "127D1C8F-D782-4F9F-A361-DD2915BB1FE5",
              "empType" : "1",
              "deviceId" : "54",
              "serviceClassId" : "1184",
              "workDate" : workDate,
              "bigClassId" : "997",
              "faultDesc" : "",
              "secMarks" : "",
              "endTime" : endTime,
              "orderType" : "105",
              "appKey" : appKey,
              "operId" : "361",
              "sourceCode" : "16",
              "activityId" : "0",
              "orderOperationRole" : "4",
              "companyId" : "263",
              "cityId" : "2222",
              "token" :token,
              "model" : "0",
              "merchantEntity" : {
                "merchantId" : "361",
                "bearTheCost" : "1"
              },
              "startTime" : startTime,
              "serviceItemEntity" : {
                "serviceItemId" : "212",
                "num" : "1",
                "serviceMoney" : "0",
                "serviceClassId" : "1184"
              },
              "channelId" : "0",
              "userAddressId" : userAddressId
            }

    m = MultipartEncoder(fields={'param': json.dumps(values)})
    r = requests.post(url_CreateThreePartOrder, m,
                      headers={'Content-Type': m.content_type}).json()
    return r

#获取订单详情
def getOrderDetailInfo(token,appKey,workOrderNo):
    requestData = {'token': token, 'appKey': appKey}  # 等于必传参数
    requestData['workOrderNo'] = workOrderNo
    requestData['operatorTypeListStr'] = '3,4'
    res = postRequest(url_GetOrderDetailInfo, requestData)
    return res

#师傅出发
def orderOrderGoto(token, appKey, workOrderId):
    requestData = {'token': token, 'appKey': appKey}  # 等于必传参数
    requestData['workOrderId'] = workOrderId  # 工作单ID
    res = postRequest(url_orderOrderGoto, requestData)
    return res
# orderOrderGoto(wgq_employeesC_token,wgq_employees_appkey,1549137)


# 师傅上门
def orderOrderService(token, appKey, workOrderId):
    requestData = {'token': token, 'appKey': appKey}  # 等于必传参数
    requestData['workOrderId'] = workOrderId  # 工作单ID
    res = postRequest(url_orderOrderService, requestData)
    return res
# orderOrderService(wgq_employeesC_token,wgq_employees_appkey,177649)
#提交订单
def orderSubmit(token, appKey, workOrderId):
    requestData = {'token': token, 'appKey': appKey}  # 等于必传参数
    requestData['workOrderId'] = workOrderId  # 工作单ID
    res = postRequest(url_orderSubmit, requestData)
    return res
# orderSubmit(wgq_employeesC_token,wgq_employees_appkey,177649)

#B端增加地址
def creat_AddAddress(localData):
    res = postRequest(url_AddAddress,localData)
    return res

#同步订单
def orderSynOrderInfoForZJ(token,appKey,workOrderNo,workOrderId):
    workOrderInfo = {"serviceClassId":1184,
                     "userId":2479926,
                     "arriveTime":1512367990000,
                     "province":"",
                     "businessId":361,
                     "parentOrderNo":"",
                     "reassignmentFlag":0,
                     "bussinessAddress":"周口市川汇区",
                     "faultDesc":"","channelId":0,
                     "headImage":"187bd8da34708756020e3f2d420a017f",
                     "activityId":0,
                     "remindFlag":0,
                     "orderStatus":6,
                     "empName":"王广强",
                     "changeReason":"",
                     "signStatus":0,
                     "longitude":114.69,
                     "vipCard":0,
                     "bussinessRelationId":36,
                     "workOrderId":workOrderId,
                     "registerMobile":"18518980784",
                     "originalPrice":0.00,
                     "empId":3184,
                     "latitude":33.64,
                     "district":"",
                     "bussinessContactName":"王强",
                     "serialVersionUID":1,
                     "dispatchTime":1512367961000,
                     "housePropertyId":0,
                     "userAddressId":28953,
                     "originalOrderNo":"",
                     "reassignmentCount":0,
                     "orderSource":16,
                     "detailAddress":"刑罗",
                     "mobileNo":"11118980000",
                     "paidMoney":0.00,
                     "bussinessName":"王广强商家",
                     "workOrderNo":workOrderNo,
                     "stationHeadId":0,
                     "thirdOrderNo":"",
                     "city":"周口",
                     "userLevelTaskDetailId":0,
                     "community":"周口师范学院",
                     "empExpectVisitTime":1512399600000,
                     "upgradeFlag":0,
                     "syncFlag":0,
                     "bookEndTime":1512401400000,
                     "stationId":35200250,
                     "extensionChannel":"",
                     "thirdCollectMoney":0.00,
                     "bussinessMobileNo":"18518980783",
                     "payableMoney":0.00,
                     "empExpectEndTime":1512401400000,
                     "combinationFlag":0,
                     "TABLE_NAME":"svc_work_order",
                     "bookStartTime":1512399600000,
                     "TABLE_ALIAS":"SvcWorkOrder",
                     "channelName":"E城E家",
                     "serviceClassName":"马桶下水疏通",
                     "payType":0,
                     "departTime":1512367973000,
                     "contactsMobile":"18518980784",
                     "reductionDetail":"",
                     "createTime":1512359224000,
                     "bussinessDictId":2,
                     "remindCount":0,
                     "adjustPriceReason":" ",
                     "syncFailTimes":0,
                     "orderType":1,
                     "contactsName":"王广强"}
    serviceItemInfo = {"combinationId":0,
                       "ecejPrice":35.00,
                       "isThreepartyMerchanCost":1,
                       "itemId":212,
                       "itemName":"马桶下水疏通-拆马桶",
                       "maintenanceChannelId":0,
                       "merchanSettleAmount":111.00,
                       "needPhotoFlag":0,
                       "orderOperationRole":4,
                       "orderType":105,
                       "paidMoney":0.00,
                       "quantity":1,
                       "receivableMoney":111.00,
                       "reductionDetail":"",
                       "serviceClassId":1184,
                       "serviceClassName":"",
                       "serviceItemId":19674,
                       "unitPrice":111.00,
                       "workOrderId":workOrderId}
    serverOrderIdentify = {"arriveLocation":"116.490282,40.012847",
                           "departLocation":"116.490282,40.012847",
                           "serverAddress":"刑罗",
                           "serverLocation":"114.689,33.6415",
                           "submitLocation":"116.490282,40.012847",
                           "submitTime":1512367997000,
                           "svcServerOrderIdentifyId":5,
                           "workOrderNo":workOrderNo}
    requestData = {'token':token,'appKey':appKey,
                    'meterOperationHistoryInfo':	[],
                    'pivotalPlaceRecord':	[],
                    'workOrderInfo':	json.dumps(workOrderInfo),
                    'protectionCardInfo':	[],
                    'housePropertyId':0,
                    'materialUsedInfo':[],
                    'mdHiddenDangerInfo':	[],
                    'hiddenDangerOrderInfo':[],
                    'serviceItemInfo':[json.dumps(serviceItemInfo)],
                    'serverOrderIdentify':json.dumps(serverOrderIdentify),
                    'securityCheckItem':[],
                    'fittingInfo':	[],
                    'meterInfo':[],
                    'online':1,
                    'equipmentInfo	':[],
                    'meterReadInfo':	[],}
    res =requests.post(url_orderSynOrderInfo,requestData)
    return res


# cookiejar = cookielib.MozillaCookieJar()
# # 将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
# cookieSupport = urllib2.HTTPCookieProcessor(cookiejar)
# # 创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的
# opener = urllib2.build_opener(cookieSupport)
# #打开图片并写
# urllib2.install_opener(opener)
#
# imgb = opener.open('http://stm.ecej.com:8081/hplatform/location/city/choose')
#
# imgName = '%s.jpg'%(str(int(time.time()))+rdmString(10))
#
# with open(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\%s' % imgName, 'wb') as f:
#     f.write(imgb.read())
#
# image = Image.open(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\%s' % imgName)
#
# vv = pytesseract.image_to_string(image)
# print vv

# os.remove(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\%s' % imgName)


# cookiejarList = []
# for i in cookiejar:
#     cookiejarList.append("%s=%s" %(i.name,i.value))
# cookies = "%s;%s"%(cookiejarList[0],cookiejarList[1])

# for index,cookie in enumerate(cookiejar):
#     cookies = cookie.name+"="+cookie.value
# cookie = cookies
#
# headers = {
#         'Cookie':cookie
#          }
#
# url_b = 'http://stm.ecej.com:8081/hplatform/configure/getCityListBySite'
#
# re = requests.post(url_b,headers=headers)
#
# url = 'http://stm.ecej.com:8081/hplatform/location/city/choose/2257'
# res = requests.post(url,headers=headers)
#
# url_a = 'http://stm.ecej.com:8081/hplatform/configure/getDeviceList/1001'
# r = requests.post(url_a,headers=headers)

