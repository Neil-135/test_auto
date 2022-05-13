import pytest
import selenium.webdriver
from time import sleep
import os
from selenium.webdriver.common.keys import Keys

chrome_path = os.path.abspath('drivers/chromedriver.exe')
url = 'http://baidu.com'

@pytest.fixture()
def open_quit():
    driver = selenium.webdriver.Chrome(executable_path=chrome_path)
    driver.maximize_window()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
    driver.find_element_by_id('su').send_keys(Keys.ENTER)
    sleep(3)
    driver.find_element_by_xpath('//*[@id="kw"]').clear()
    sleep(3)
    yield driver
    driver.quit()

def test_case_1(open_quit):
    print('\n 开始执行测试用例！')
    driver = open_quit
    print('got data:',driver)

    print('\n 测试用例执行完毕！')
    assert True

if __name__ == '__main__':
    args = ['-s','-q','test_lianxi.py']
    pytest.main(args)

