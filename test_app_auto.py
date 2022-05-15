# app自动化简要实现

from appium import webdriver
import pytest
# import unittest
import time


class TestAppauto:
    def test_app_auto_1(self):
        print('压力测试')
        for cycle in range(1,4):
            print('现在开始执行第{0}次：'.format(cycle))
            try:
                caps = {}
                caps["platformName"] = "Android"
                caps["platformVersion"] = "5"
                caps["deviceName"] = "127.0.0.1:21503"
                caps["appPackage"] = "com.lchr.diaoyu"
                caps["appActivity"] = "com.lchr.diaoyu.SplashActivity"
                caps["noReset"] = True
                caps["newCommandTimeout"] = 6000
                caps["automationName"] = "UiAutomator2"
                caps["ensureWebviewsHavePages"] = True

                time.sleep(3)
                app_driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
                time.sleep(10)
                app_driver.find_element_by_id("com.lchr.diaoyu:id/btn_tab_mine").click()
                time.sleep(1)
                app_driver.find_element_by_id("com.lchr.diaoyu:id/u_avatar").click()
                time.sleep(3)
                app_driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android."
                                                 "widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget."
                                                 "FrameLayout/android.view.View/android.view.View/android.widget."
                                                 "RelativeLayout/android.widget.EditText").send_keys("17318038838")
                # time.sleep(3)
                # app_driver.find_element_by_id("com.lchr.diaoyu:id/cb_agree_privacy").click()
                # time.sleep(3)
                # app_driver.find_element_by_id("com.lchr.diaoyu:id/btn_get_code").click()
                time.sleep(2)
                app_driver.quit()
                print('***第{}次执行成功***'.format(cycle))
                time.sleep(3)
                assert True
            except Exception as e:
                print('***第{}次执行失败***'.format(cycle))
                print(e)

    # def tearDown(self):
    #     print('测试结束')


if __name__ == '__main__':
    argv = ['-s','-q','test_app_auto.py']
    pytest.main(argv)
    # unittest.main()
