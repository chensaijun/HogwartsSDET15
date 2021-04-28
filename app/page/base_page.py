#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver =None):
        self.driver = driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def find_and_click(self,by,locator):
        self.driver.find_element(by,locator).click()

    def find_and_sendkeys(self,by,locator,value):
        self.driver.find_element(by,locator).send_keys(value)

    def get_scholl(self,text):
        # 滚动查找到某个元素后点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector()\
                                        .scrollable(true).instance(0))\
                                        .scrollIntoView(new UiSelector()\
                                        .text("{text}").instance(0));').click()