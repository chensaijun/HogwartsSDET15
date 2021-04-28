#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.edit_member_page import EditMemberPage


class MemberDetailsPage(BasePage):
    def member_details(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='编辑成员']")
        return EditMemberPage(self.driver)
