#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium import webdriver


class TestTX:
    def setup(self):
        disired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()