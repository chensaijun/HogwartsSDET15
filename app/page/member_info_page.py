#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.member_details_page import MemberDetailsPage


class MemberInfoPage(BasePage):
    def member_info(self):
        self.find_and_click(MobileBy.ID,"com.tencent.wework:id/h8g")
        return MemberDetailsPage(self.driver)
