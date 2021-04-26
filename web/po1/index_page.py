#! /usr/bin/python 3
# -*- coding:UTF8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from homework.po1.importmenber_page import  ImportMenberPage


class IndexPage:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.implicitly_wait(5)

    def goto_Importmenber(self):
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        return ImportMenberPage(self.driver)