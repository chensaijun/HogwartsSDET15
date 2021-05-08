#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from frame.handle_black import handle_black


class BasePage:
    black_list = [(MobileBy.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/iv_close']")]
    # black_list = [(MobileBy.XPATH, "//*[contains(@text,'跳过广告')]")]
    max_num = 3
    err_num = 0
    def __init__(self, driver: WebDriver = None):
        """
        初始化
        :param driver:
        """
        if driver == None:
            disired_caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,
                # "dontStopAppOnReset": True,
                # "skipDeviceInitialization": True,
                # "unicodeKeyBoard": True,
                # "resetKeyBoard": True,
                # 'skipServerInstallation': 'true',
                # sdk自带，通过android stuio创建的模拟器，自动启动模拟器
                # 'avd':'模拟器名称'
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            # 如果传的元素是一个，只有by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是两个，既有by，又有locator
            result = self.driver.find_element(by,locator)
        return result

        # try:
        #     if locator == None:
        #         # 如果传的元素是一个，只有by
        #         result = self.driver.find_element(*by)
        #     else:
        #         # 如果传的元素是两个，既有by，又有locator
        #         result = self.driver.find_element(by,locator)
        #     self.err_num = 0
        #     return result
        # # 捕获黑名单中的元素
        # except Exception as e:
        #     # 超过最大查找次数
        #     if self.err_num > self.max_num:
        #         raise e
        #     self.err_num += 1
        #     # 从黑名单中遍历元素，依次进行处理
        #     for black_ele in self.black_list:
        #         ele = self.driver.find_elements(*black_ele)
        #         if len(ele)>0:
        #             ele[0].click()
        #             # 处理完黑名单后，再次查找原来的元素
        #             return self.find(by,locator)
        #     raise e


    def parse_yaml(self,path,func_name):
        with open(path,encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])


    def parse(self,steps):
        """
        解析yaml内容
        :param steps:
        :return:
        """
        # 遍历每一个步骤
        for step in steps:
            # 如果是点击
            if 'click' == step['action']:
                self.find(step['by'],step['locator']).click()
            #如果是输入文本
            elif 'send' == step['action']:
                self.find(step['by'],step['locator']).send_keys(step["content"])
