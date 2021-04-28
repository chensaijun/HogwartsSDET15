#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.base_page import BasePage


class EditMemberPage(BasePage):
    def edit_member(self):
        # 点击删除成员按钮
        self.get_scholl("删除成员")
        self.find_and_click(MobileBy.ID,"com.tencent.wework:id/bei")

