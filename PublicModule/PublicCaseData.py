#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

import sys
import os


from PublicModule.PublicClass import *

# 数据灵活设置，防止环境切换或数据清理
#登陆账号
tel = 18518980784
password = '25F9E794323B453885F5181F1B624D0B'

#用户端
wgq_token = '633eafd256044ea98cb956c11239a247'
wgq_appkey = '20171106175629d97173e14b47b705df0a34d3504f58f7'

wjb_token = 'a7e51662679e449b82579bf9411bb259'
wjb_appKey = '20171109141913a78e933bc50491b0596b1bf8bc1f94f7'

#员工端
wgq_employees_appkey = '20171109182338b8597fb7bfa41b5d8820e73ab15e41e7'
wgq_employees_userId = '5106'
wgq_employeesC_token = '4a89479b3b99432a9e1caed8a974168c'

#用户端host
userAppHost1 = 'http://stbs.ecej.com:8081'
userAppHost2 = 'http://ststark.ecej.com:8081'
#员工端host
employeesAppHost1 = 'http://stemp.ecej.com:8081'
employeesAppHost2 = 'https://stemp.ecej.com'

#接口地址 商家
url_LoginIndex = userAppHost1+'/bapp/v1/login/loginIndex'#登陆接口
url_Count = userAppHost2+'/threeparty/orderQuery/count'#我的详情
url_CityListBybussinessInfo = userAppHost1+'/bapp/v1/bussiness/cityListBybussinessInfo'#根据商户ID获取商户服务的城市
url_Device = userAppHost1+'/bapp/v1/bbs/device'#在线的设备接口
url_ServiceClassAndItem = userAppHost1+'/bapp/v1/bbs/serviceClassAndItem'#B端在线的品类项目接口
url_AddAddress = userAppHost1+'/bapp/v1/address/addAddress'#创建地址
url_GetRecommendTime = userAppHost1+'/bapp/v1/recomment/getRecommendTime'#获取推荐时间接口
url_CreateThreePartOrder = userAppHost2+'/threeparty/createThreePartOrder'#创建订单接口
url_GetTimeListHead = userAppHost1+'/bapp/v1/recomment/getTimeListHead'#根据城市ID获取预约天数
url_RecommentLockEmp = userAppHost1+'/bapp/v1/recomment/lockEmp'#锁定师傅
url_SelectAppointmentTime = userAppHost1+'/bapp/v1/recomment/selectAppointmentTime'#查询预约时间
url_GetOrderDetailInfo = userAppHost2+'/threeparty/orderQuery/getOrderDetailInfo'#查看订单详情
url_GetOrderList = userAppHost2+'/threeparty/orderQuery/getOrderList'#获取订单列表
url_Logout = userAppHost1+'/bapp/v1/login/logout'#退出登录

#接口地址 用户端

url_orderOrderGoto = employeesAppHost2 + "/v1/order/orderGoto" #商城下单（上门服务）-师傅出发
url_orderOrderService = employeesAppHost2 + "/v1/order/orderService" #商城下单（上门服务）-师傅上门
url_orderSubmit = employeesAppHost2 +'/v1/order/submit'#提交
url_orderSingleDownload = employeesAppHost2+'/v1/order/singleDownload'#下载同步
url_orderSynOrderInfo = employeesAppHost2+'/v1/order/synOrderInfo'#同步订单状态
url_CaptchaImage = 'https://st1busplatform.ecej.com/site/captchaImage?_=0.04913981744982122'


# 邮件相关参数
user = '707958420@qq.com' #邮箱账号
pwd  = 'pjxorgckfzfvbeib' #邮箱授权口令
to= ['wanggqe@ecej.com'] #接收方
sentSevice = "smtp.qq.com:465" #邮件服务器地址



#万佳彬B端下单地址
wjb_create_addAddress_localData = {
            'appKey': wjb_appKey,
            'districtInfo': u"community:河西花园,latitude:23.09058076556858,longitude:113.17565167542321",
            'token': wjb_token,
            'districtName': u'南海区',
            'phone': 18600031200,
            'userName': u'哈哈',
            'cityName': u'佛山市',
            'cityId': 128,
            'detailAddress': u'测试地址' + str(random.random())
        }



LoginUrl = "http://stadm.ecej.com:8081/login/login"
vrifycodeUrl = "https://stbusplatform.ecej.com/site/captchaImage"
#
# headers = {
#             'Host': 'st1platform.ecej.com:8081',
#             'Connection': 'keep-alive',
#             'Accept': 'application/json, text/plain, */*',
#             'X-Requested-With': 'XMLHttpRequest',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#             'Referer': 'http://st1platform.ecej.com:8081/base/html/nav.html',
#             'Accept-Encoding': 'gzip, deflate, sdch',
#             'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#             'Cookie': 'UM_distinctid=15f37c27189bb-0f2902f15f508e-5d4e211f-1fa400-15f37c2718a6a2; SESSION=4d11e062-099c-45b4-8a51-a709ffe8d68f'
# }
# url = 'http://st1platform.ecej.com:8081/base/getLoginName'
# res = requests.get(LoginUrl,headers = headers)
# print res

