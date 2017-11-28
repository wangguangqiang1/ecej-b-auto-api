#! /user/bin/evn python
# coding:utf-8
'''
@author: 'luoyun'
@file: testlogin.py
@time: 2017/11/15 14:06
'''

#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from PIL import Image,ImageEnhance
import pytesseract
import os
import pytesseract
# os.chdir(os.path.abspath('E:\ecej-b-auto-test\pytesser_v0.0.1' ))
os.chdir(os.path.abspath('%s../../pytesser_v0.0.1' % os.path.split(os.path.realpath(__file__))[0]))

def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login.png')  #截取商家后台登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgLocation = imgElement.location #获取验证码元素坐标
    # print imgLocation
    # rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    rangle = (960, 553, int(960 + imgSize['width']+20),int(553 + imgSize['height'] +20))
    login = Image.open("login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('login.png')
    authcodeImg = Image.open('login.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    # os.remove(os.path.abspath('%s../../publicImage/%s' % (os.path.split(os.path.realpath(__file__))[0],imgName)))
    return authCodeText

def pandarola_login(driver,account,passwd,authCode):
    '''登录pandarola系统'''
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[1]/div/div/div[1]/input').send_keys(account)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[2]/div/div/div[1]/input').send_keys(passwd)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input').send_keys(authCode)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/div/div/button').click()

    # title = driver.find_element_by_id('menuName-h').text  #获取登录的标题
    # '''验证是否登录成功'''
    # try:
    #     assert title == u'桌面'
    #     return '登录成功'
    # except AssertionError as e:
    #     return '登录失败'

if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get('https://stbusplatform.ecej.com/site/login')
    driver.maximize_window()
    time.sleep(3)
    # driver.get_screenshot_as_file('F:\\login1.png')
    imgElement = driver.find_element_by_id("captchaImg")
    authCodeText = get_auth_code(driver,imgElement)
    pandarola_login(driver,'18600031200','123456',authCodeText)
    # driver.quit()
