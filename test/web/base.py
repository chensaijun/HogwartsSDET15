#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from selenium import webdriver


class Base:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()