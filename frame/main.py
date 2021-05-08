#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.basepage import BasePage
from frame.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find(MobileBy.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/post_status']").click()
        # self.find(MobileBy.XPATH, "//*[@resource-id = 'android:id/tabs']//*[@text = '行情']").click()
        self.parse_yaml("./main.yaml", "goto_market")
        return Market(self.driver)
