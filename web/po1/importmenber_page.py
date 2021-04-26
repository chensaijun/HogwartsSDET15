#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from selenium.webdriver.remote.webdriver import WebDriver


class ImportMenberPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def Importmenber(self):
        self.driver.find_element_by_css_selector(".js_go_template_import").click()
        self.driver.find_element_by_css_selector(".ww_fileImporter_fileContainer_uploadInputMask").send_keys("C:/Users/1/PycharmProjects/practice_and_homework/practice/web/demo.xlsx")
        self.driver.find_element_by_css_selector(".ww_fileImporter_submitWrap>a").click()
        return True