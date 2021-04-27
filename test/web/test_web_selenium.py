#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from time import sleep

import action
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class Test():
    # ActionChains
    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     # 最大化浏览器
    #     self.driver.maximize_window()
    #     # 隐式等待
    #     self.driver.implicitly_wait(3)

    # touchactions
    def setup_class(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)

        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value = 'click me']")
        element_duble_click = self.driver.find_element_by_xpath("//input[@value = 'dbl click me']")
        element_dright_click = self.driver.find_element_by_xpath("//input[@value = 'right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_duble_click)
        action.context_click(element_dright_click)
        action.perform()

    def test_move(self):
        # 光标移动到某个位置上
        self.driver.get("http://www.baidu.com")
        element_move = self.driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(element_move)
        action.perform()
        sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop)
        action.perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        # pouse 暂停
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(3)

    def test_touchAction(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_xpath("//*[@id='kw']")
        el = self.driver.find_element_by_xpath("//*[@id='su']")
        ele.click()
        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el)
        action.perform()
        action.scroll_from_element(ele, 0, 1000).perform()

        sleep(3)


if __name__ == '__main__':
    pytest.main('-v', '-s', 'test_web_selenium.py')
