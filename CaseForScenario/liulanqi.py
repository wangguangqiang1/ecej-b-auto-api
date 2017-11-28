#! /user/bin/evn python
# coding:utf-8

__author__ = 'wgq'

import time
import os
from selenium import webdriver

from webbrowser import browser
import random
import pytesseract
from PIL import Image,ImageEnhance

def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\login.png')  #截取商家后台登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    # rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    rangle = (960, 553, int(960 + imgSize['width']+20),int(553 + imgSize['height'] +20))
    login = Image.open(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\login.png')
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\login.png')
    authcodeImg = Image.open(r'C:\Users\admin\PycharmProjects\ecej-B-auto-test\publicImage\login.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    # os.remove(os.path.abspath('%s../../publicImage/%s' % (os.path.split(os.path.realpath(__file__))[0],imgName)))
    return authCodeText

def pandarola_login(driver,authCode):
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[1]/div/div/div[1]/input").send_keys("18518980784")
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys("123456789")
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input').send_keys(authCode)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[4]/div/div/button").click()
    driver.find_element_by_link_text("我要下单").click()
    driver.find_element_by_xpath("/html/body/div[16]/div/div[1]/div[2]/div[2]/div/form/div[2]/div[3]/div/div/div/input").send_keys("18518980784")
    driver.find_element_by_xpath("/html/body/div[16]/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/div/div[1]/div/div/div/div[1]/i").click()
    driver.find_element_by_xpath("/html/body/div[17]/div/div[1]/ul/li/span").click()
    driver.find_element_by_xpath("/html/body/div[16]/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/div/div[2]/div/div/div/div").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[16]/div/div[2]/div/div[2]/div[2]/div[2]/div/input").send_keys(u'周口师范学院')
    sreach_window=driver.current_window_handle
    time.sleep(3)
    # for handle in driver.window_handles:#方法二，始终获得当前最后的窗口，所以多要多次使用
    #     driver.switch_to_window(handle)

    driver.find_element_by_xpath("/html/body/div[16]/div/div[2]/div/div[2]/div[3]/div/ul/li[2]/p[1]").click()

    driver.find_element_by_xpath("/html/body/div[16]/div/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/div/div[3]/div/div/div/input").send_keys(random.randint(1,100)),
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[16]/div/div[1]/div[2]/div[2]/div/form/div[4]/div/div/div/button").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div/div[3]/div/div/div/div[1]/i").click()
    driver.find_element_by_xpath("/html/body/div[6]/div/div[1]/ul/li[2]").click()
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div/div[5]/div/div/div/div[1]/i").click()
    driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/ul/li[3]/span").click()
    driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div[2]/div[2]/div/form/div[1]/div/div/div[7]/div/div/div/div[1]/i").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[8]/div/div[1]/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element_by_id('submitId').click()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://stbusplatform.ecej.com/site/login')
    driver.maximize_window()
    imgElement = driver.find_element_by_id("captchaImg")
    authCodeText = get_auth_code(driver,imgElement)
    pandarola_login(driver,authCodeText)