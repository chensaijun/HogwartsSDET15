#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from app.page.app import App


class TestDeleteMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_mainpage()
    def test_delete_member(self):
        username = "aa-11"
        self.main.goto_address1().get_member(username).member_info().member_details().edit_member()
        result = self.app.driver.page_source
        assert username not in result