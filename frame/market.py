#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.basepage import BasePage
from frame.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(MobileBy.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("./market.yaml", "goto_search")
        return Search(self.driver)