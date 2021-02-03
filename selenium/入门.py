#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 浏览器前进/后退
driver = webdriver.Chrome()
qaurl = 'http://admin.cps26.dzods.cn/'  #   26测试环境地址
driver.get(qaurl)
print("now access %s"%qaurl)
time.sleep(5)

#   访问新的页面
newurl = 'http://www.baidu.com/'
driver.get(newurl)
print("new access %s"%newurl)
time.sleep(3)

#   返回26测试环境
driver.back()
print("back access %s"%qaurl)
time.sleep(3)

#  返回百度URL
driver.forward()
print("forward access %s"%newurl)
time.sleep(3)

driver.quit()

## driver.maximize_window()    #浏览器窗口最大化
# driver.set_window_size(1000,500)     #设置浏览器窗口宽高
# driver.find_element_by_xpath('//*[@id="carousel-example-generic"]/div/div/p/a').click()
# time.sleep(3)
# driver.find_element_by_id('pd-form-username').send_keys('admin')
# driver.find_element_by_id('pd-form-password').send_keys('Aa123456')
# driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/button').click()
# print(driver.title)         #  浏览器打印title
# time.sleep(3)
# driver.quit()

