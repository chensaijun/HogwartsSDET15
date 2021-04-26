#! /usr/bin/python 3
# -*- coding:UTF8 -*-
"""
使用PO 封装首页和添加成员页，
首页点击 联系人， 再点击添加成员，完成添加成员功能。并验证添加成功。

完成添加联系人功能，使用显式等待隐式等待结合的方式，练习课上的知识点。
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.po2.add_member import AddMemberPage
from web.po2.base import Base


class MainPage(Base):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
    #     self.driver.implicitly_wait(5)

    def goto_addmember(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)

    def goto_addmember1(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) a:nth-child(2)").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) a:nth-child(2)")
        # sleep(3)
        # 显示等待
        # element:WebElement = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator)
        # element.click()

        # 尝试多次点击，知道进入添加联系人页面
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID,"username")
            except:
                return False
        WebDriverWait(self.driver,10).until(wait_for_next)

        return AddMemberPage(self.driver)
