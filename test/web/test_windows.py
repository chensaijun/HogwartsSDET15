#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from time import sleep

from selenium import webdriver

from practice.web.base import Base


class TestWindows(Base):
    def test_windows(self):
        # 多窗口切换
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='s-top-loginbtn']").click()
        self.driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a").click()
        # 获取当前窗口句柄
        print(self.driver.current_window_handle)
        # 获取所有窗口句柄
        print(self.driver.window_handles)
        window = self.driver.window_handles
        # 切换到某个窗口进行操作
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15100000000")
        sleep(3)

        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

