#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import pytest
from appium import webdriver


class TestSeacher:
    """
    noReset  在当前 session 下不会重置应用的状态
    dontStopAppOnReset  在使用 adb 启动应用之前，不要终止被测应用的进程
    skipDeviceInitialization  启动时跳过初始化设置
    unicodeKeyBoard  使用 Unicode 输入法
    resetKeyBoard  在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态


    """
    def setup(self):
        disired_caps={
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset":True,
            "dontStopAppOnReset":True,
            "skipDeviceInitialization":True,
            "unicodeKeyBoard":True,
            "resetKeyBoard":True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",disired_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):

        self.driver.quit()

    def test_seacher(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price >200

if __name__ == '__main__':
    pytest.main()
