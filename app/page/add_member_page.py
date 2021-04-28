#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member_page1(self, username, phonenum):
        # 快速添加联系人
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']",
                               username)
        self.find_and_sendkeys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text= '必填']", phonenum)
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'保存')]")

        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
