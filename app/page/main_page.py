#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.page.base_page import BasePage
from app.page.member_invite_menu_page import MemberInviteMenuPage


class MainPage(BasePage):

    def goto_address(self):
        # 进入通讯录页面
        self.find_and_click(MobileBy.XPATH,"//*[@text = '通讯录']")
        # 滚动页面查找添加成员入口
        self.get_scholl("添加成员")
        return MemberInviteMenuPage(self.driver)

    def goto_address1(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text = '通讯录']")
        return MemberInviteMenuPage(self.driver)







