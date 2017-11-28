#! /user/bin/evn python
# coding:utf-8


__author__ = 'wgq'

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ecej.ui'
desired_caps['appActivity'] = '.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.find_element_by_id('com.ecej.ui:id/rbMine').click()

driver.find_element_by_id('com.ecej.ui:id/btnLogini').click()
time.sleep(2)
driver.find_element_by_id('com.ecej.ui:id/tvAccountPwdLogin').click()
driver.find_element_by_id('com.ecej.ui:id/edUserName').send_keys('18518980784')
driver.find_element_by_id('com.ecej.ui:id/edPassword').send_keys('910520')
driver.find_element_by_id('com.ecej.ui:id/btLogin').click()

driver.find_element_by_name('卫生间').click()
# driver.find_elements_by_xpath('//FrameLayout/ScrollView.TextView/android.support.v4.view.ViewPager/android.widget.RelativeLayout[contains(@resource-id, 'android.widget.RelativeLayout')]')
driver.find_element_by_name('水龙头2.0').click()
driver.find_element_by_id('com.ecej.ui:id/tv_visit_order_bottom_overbooking').click()
time.sleep(2)
driver.find_element_by_id('com.ecej.ui:id/tv_write_order_bottom_overbooking').click()

# driver.quit()