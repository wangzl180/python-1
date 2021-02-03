from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
dr = webdriver.Chrome()
url = 'https://e.tyrise.com'
dr.get(url)
dr.maximize_window()
#登录
dr.find_element_by_xpath('//*[@id="app"]/main/section/div/div[2]/div[1]/div/input').send_keys('admin')
dr.find_element_by_xpath('//*[@id="app"]/main/section/div/div[2]/div[2]/div/input').send_keys('tyrise233')
dr.find_element_by_xpath('//*[@id="app"]/main/section/div/div[2]/button').click()
dr.implicitly_wait(5)

dr.find_element_by_link_text('代理商').click() # 文字点击代理商
dr.implicitly_wait(3)
dr.find_elements_by_class_name('handle-title')[4].click()  #点击爪马
dr.implicitly_wait(5)

#跳转至爪马代理登录下
dr.switch_to.window(dr.window_handles[1]) # 定位当前页面
dr.find_element_by_link_text('客户').click()
dr.implicitly_wait(3)
dr.find_elements_by_class_name('handle-title')[2].click() #点击Android应用下载
dr.implicitly_wait(5)

#进入客户Android应用下载 登录状态下
dr.switch_to.window(dr.window_handles[2]) # 定位当前页面
dr.find_element_by_link_text('推广').click()   #点击推广界面
dr.implicitly_wait(3)

dr.find_element_by_xpath('//*[@id="pane-group"]/div/div[1]/div[1]/div[1]/div[2]/div/button[3]/span').click() #点击新建广告组
dr.implicitly_wait(2)