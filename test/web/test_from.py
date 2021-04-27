#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from time import sleep

from selenium import webdriver


class TestFrom:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_from(self):
        self.driver.get("http://10.4.24.172:20001/#/user/login")
        self.driver.find_element_by_xpath("//*[@id='userName']").send_keys("18000000007")
        self.driver.find_element_by_id("password").send_keys("123456a")
        self.driver.find_element_by_id("verifyCode").send_keys("f2nf")
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/div/form/button").click()
        sleep(3)
        self.driver.find_element_by_id("stfile").send_keys("C:\Users\1\PycharmProjects\practice_and_homework\practice\web\image\果蔬脆透明底 (1).png")
