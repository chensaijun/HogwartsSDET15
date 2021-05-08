#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestXQ:
    def setup(self):
        disired_caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset":True,
            # "dontStopAppOnReset":True,
            "skipDeviceInitialization":True,
            "unicodeKeyBoard":True,
            "resetKeyBoard":True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",disired_caps)
        self.driver.implicitly_wait(10)

    def test_search_xueqiu(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,"//*[@text = 'BABA']/../../..//*[@resource-id ='com.xueqiu.android:id/current_price']").text)
        expect_price = 220
        assert_that(current_price,close_to(expect_price,expect_price*0.1))

    @pytest.mark.parametrize("searchkey,type,expect_price",
                             [
                                 ("alibaba","BABA",220),
                                 ("xiaomi","01810",20)
                             ])
    def test_search_xq(self,searchkey,type,expect_price):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("searchkey")
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,
                                                       "//*[@text = 'type']/../../..//*[@resource-id ='com.xueqiu.android:id/current_price']").text)
        # expect_price = 220
        print(f"当前价格：{current_price}")
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
