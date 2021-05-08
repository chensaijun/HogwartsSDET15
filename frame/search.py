#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from frame.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.find(MobileBy.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        self.parse_yaml("./search.yaml", "search")