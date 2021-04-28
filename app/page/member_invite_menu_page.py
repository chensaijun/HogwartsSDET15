#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


from app.page.base_page import BasePage
from app.page.member_info_page import MemberInfoPage


class MemberInviteMenuPage(BasePage):

    def member_invite_menu_page(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")

        from app.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def get_toast(self):
        result = self.find(MobileBy.XPATH,"//*[@class = 'android.widget.Toast']").text
        return result

    def get_member(self,username):
        # 定位要删除的用户，点击进入个人信息页面
        self.find_and_click(MobileBy.XPATH,f"//*[@text = '{username}']")
        return MemberInfoPage(self.driver)