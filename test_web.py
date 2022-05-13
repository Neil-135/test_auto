# python selenium一般使用方法

import selenium.webdriver
import os.path
import pytest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


chrome_path = os.path.abspath('drivers/chromedriver.exe')
# firefox_path = os.path.abspath('drivers/geckodriver.exe')
# ie_path = os.path.abspath('drivers/IEDriverServer.exe')
# print(firefox_path)
url = 'http://www.baidu.com'
# url1 = 'http://qzone.qq.com/index.html'
# url2 = 'http://jrj.com.cn'
# checkbox_file_path = 'file:///'+os.path.abspath('checkbox.html')
# fileupload_file_path = 'file:///'+os.path.abspath('fileUpload.html')
# dropdown_file_path = 'file:///'+os.path.abspath('drop_down.html')
alert_file_path = 'file:///'+os.path.abspath('alert.html')


@pytest.fixture()
def open_quit():
    option = selenium.webdriver.ChromeOptions()
    # 无界面运行
    # option.add_argument('--headless')

    # 窗口最大化运行
    # option.add_argument('--start-maximized')

    # 隐身模式运行（无痕模式）
    # option.add_argument('--incognito')

    # 不展示“浏览器正在被自动化程序控制”提示
    # option.add_argument('--disable-infobars')
    # option.add_experimental_option("excludeSwitches", ["enable-automation"])
    # option.add_experimental_option('useAutomationExtension', False)

    driver = selenium.webdriver.Chrome(executable_path=chrome_path)
    # driver = selenium.webdriver.Firefox(executable_path=firefox_path)
    # driver = selenium.webdriver.Ie(executable_path=ie_path)
    # driver.implicitly_wait(30)

    # 窗口最大化运行
    driver.maximize_window()
    # driver.get(checkbox_file_path)
    driver.get(alert_file_path)
    # driver.get(url2)
    time.sleep(6)
    yield driver
    driver.quit()

def test_my_web(open_quit):
    print('\n 开始执行测试用例')
    driver = open_quit
    print('got driver: ',driver)
    # 通过id定位
    # driver.find_element_by_id('kw').send_keys('tomy')
    # time.sleep(2)

    # 通过name定位
    # driver.find_element_by_name('wd')
    # time.sleep(2)

    # 使用tag_name定位
    # driver.find_element_by_tag_name('input').send_keys('selenium')  定位失败

    # 使用class_name定位
    # driver.find_element_by_class_name('s_ipt').send_keys('selenium')
    # time.sleep(2)

    # 通过使用开发者工具复制css路径
    # driver.find_element_by_css_selector('#kw').send_keys('selenium')
    # time.sleep(2)

    # 使用css定位，手写css
    # driver.find_element_by_css_selector('input.s_ipt').send_keys('selenium')
    # time.sleep(2)

    # 使用class结合id定位
    # driver.find_element_by_css_selector('input#kw.s_ipt').send_keys('selenium')
    # time.sleep(2)

    # link_text定位
    # driver.find_element_by_link_text('新闻').click()
    # time.sleep(2)

    #partial_link_text定位
    # driver.find_element_by_partial_link_text('新').click()
    # time.sleep(2)

    # back and forward
    # element = driver.find_element_by_id('kw')
    # element.send_keys('selenium')
    # time.sleep(2)
    # clear清除搜索的输入内容
    # element.clear()
    # time.sleep(2)
    # element.send_keys('python')
    # 类似于点击百度一下进行搜索
    # driver.find_element_by_id('su').submit()

    # driver.find_element_by_id('kw').click()
    # time.sleep(2)
    # driver.back()
    # time.sleep(3)
    # driver.forward()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # driver.forward()
    # time.sleep(2)

    # 获取text值
    # element = driver.find_element_by_xpath('//div[contains(text(),"热搜")]')
    # print('got text: ',element.text)
    # time.sleep(2)

    # Keys.ENTER 方法使用
    # driver.find_element_by_id('kw').send_keys('python')
    # time.sleep(2)
    # element = driver.find_element_by_id('su')
    # element.send_keys(Keys.ENTER)
    # time.sleep(2)

    #  打印
    # print('title: ',driver.title)
    # print('current url: ',driver.current_url)

    # 以百度首页为例，对右键菜单的操作(右键地图按钮选择在新窗口打开)
    # element = driver.find_element_by_link_text('地图')
    # time.sleep(2)
    # ActionChains(driver).context_click(element).perform()
    # pyautogui.typewrite(['down','down','return'])
    # time.sleep(3)

    # 对一组元素操作：对checkbox.html中一组复选框操作
    # inputs = driver.find_elements_by_tag_name('input')
    # for input in inputs:
    #     if input.get_attribute('type') == 'checkbox':
    #         input.click()
    # time.sleep(2)

    # 切换框架iframe
    # driver.switch_to.frame('login_frame')
    # driver.find_element_by_id('switcher_plogin').click()
    # time.sleep(2)

    # 切换窗口
    # driver.find_element_by_link_text('登录').click()
    # 使用绝对路径xpath定位
    # driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div/ul/li/a[@class="hover"]').click()
    # 使用相对路径xpath定位
    # driver.find_element_by_xpath('//div/div[2]/div/ul/li/a[@class="hover"]').click()
    # time.sleep(2)
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.find_element_by_id('txtUsername').send_keys('neil')
    # driver.find_element_by_id('txtPassword').send_keys('123456')
    # time.sleep(2)
    # driver.find_element_by_link_text('登 录').click()
    # time.sleep(2)

    # 使用层级定位页面元素
    # driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div/div[3]/div/a/div').click()
    # time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div/div/div[5]/div/div/div[3]/ul/li/a/span[2]').click()
    # time.sleep(3)
    # father = driver.find_element_by_id('hotsearch-content-wrapper')
    # father.find_elements_by_tag_name('span')[1].click()
    # time.sleep(3)
    # driver.get('https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%23')
    # driver.find_element_by_xpath('//div/div/table/tbody/tr[2]/td/a').click()
    # time.sleep(3)

    # 文件上传操作
    # driver.find_element_by_id('file').send_keys(os.path.abspath('checkbox.html'))
    # time.sleep(3)

    # 下拉框操作
    # element = driver.find_element_by_name('辛弃疾')
    # Select(element).select_by_value('02')
    # Select(element).select_by_index('5') # 索引与切片
    # Select(element).select_by_visible_text('马作的卢飞快，弓如霹雳弦惊。')
    # time.sleep(3)

    # alert 提示框操作
    # driver.find_element_by_id('alert').click()
    # time.sleep(2)
    # driver.switch_to.alert.accept()
    # time.sleep(3)

    # confirm 提示框操作
    # driver.find_element_by_id('confirm').click()
    # time.sleep(2)
    # driver.switch_to.alert.accept()
    # # driver.switch_to.alert.dismiss()
    # time.sleep(3)

    # prompt 提示框操作
    driver.find_element_by_id('prompt').click()
    time.sleep(2)
    driver.switch_to.alert.send_keys('python')
    driver.switch_to.alert.accept()
    # driver.switch_to.alert.dismiss()
    time.sleep(3)

    # 执行js脚本
    # driver.find_element_by_id('kw').send_keys('selenium')
    # driver.find_element_by_id('su').click()
    # time.sleep(3)
    # js = 'window.scrollTo(0,document.body.scrollHeight)'
    # driver.execute_script(js)
    # time.sleep(2)
    # js = 'window.scrollTo(0,document.body.scrollTop=0)'
    # driver.execute_script(js)
    # time.sleep(3)

    print('\n 测试用例执行完毕！')
    assert True

if __name__ == '__main__':
    args = ['-s','-q','test_web.py']
    pytest.main(args)